from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET', 'DELETE', 'PUT']) # Methods Allowed
@permission_classes((IsAuthenticated, IsOwnerOrReadOnly,)) # Pemissions, Only Authenticated user
def get_delete_update_movie(request, pk):  #pk es PrimaryKey(Id)
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # details a sinlge movie
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    # delete a movie
    elif request.method == 'DELETE':
        if(request.user == movie.creator): # If creator is who makes request
            movie.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
    # update a movie
    elif request.method == 'PUT':
        if(request.user == movie.creator): # If creator is who makes request
            data = JSONParser().parse(request)
            serializer = MovieSerializer(movie, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def get_post_movies(request):
    # get all movies
    if request.method == 'GET':
        puppies = Movie.objects.all()
        serializer = MovieSerializer(puppies, many=True)
        return Response(serializer.data)

    # create a new movie
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

