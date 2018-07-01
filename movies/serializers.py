from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User



class MovieSerializer(serializers.ModelSerializer): # create classs to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer): #create class to serealizer usermodel
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')