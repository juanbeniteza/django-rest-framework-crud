from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/movies/(?P<pk>[0-9]+)$', # urls with details i.e /movies/(1-9)
        views.get_delete_update_movie.as_view(),
        name='get_delete_update_movie'
    ),
    url(
        r'^api/v1/movies/$', # urls list all and create new one
        views.get_post_movies.as_view(),
        name='get_post_movies'
    )
]