from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_movie(request, pk):  #pk es PrimaryKey(Id)
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # obtiene los detalles de una movie individual
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    # borra una movie
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # actualiza una movie
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_movies(request):
    # todas las  movies
    if request.method == 'GET':
        puppies = Movie.objects.all()
        serializer = MovieSerializer(puppies, many=True)
        return Response(serializer.data)

    # insertando nueva movie
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

