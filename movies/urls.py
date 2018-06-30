from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/movies/(?P<pk>[0-9]+)$',
        views.get_delete_update_movie,
        name='get_delete_update_movie'
    ),
    url(
        r'^api/v1/movies/$',
        views.get_post_movies,
        name='get_post_movies'
    )
]