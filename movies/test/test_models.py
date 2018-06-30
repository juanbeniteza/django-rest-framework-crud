from django.test import TestCase
from ..models import Movie


class MovieTest(TestCase):
    """ Test module for Movie model """

    def setUp(self):
        Movie.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Movie.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')