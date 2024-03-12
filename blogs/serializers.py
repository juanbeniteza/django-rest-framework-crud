from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Blog
        fields = ('id', 'topic','title','content','image', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'blogs')
