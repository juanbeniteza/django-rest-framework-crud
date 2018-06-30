from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer): # Definimos la clase para serialziar el modelo
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'year', 'created_at', 'updated_at') # definimos que campos usar


