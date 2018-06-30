#from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single movie
    if request.method == 'GET':
        return Response({})
    # delete a single movie
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single movie
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_movies(request):
    # todas las  movies
    if request.method == 'GET':
        puppies = Movie.objects.all()
        serializer = MovieSerializer(puppies, many=True)
        return Response(serializer.data)

    # insertando nueva movie
    elif request.method == 'POST':
        return Response({})

