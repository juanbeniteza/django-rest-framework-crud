
from django.contrib import admin
from django.conf.urls import include, url


# urls
urlpatterns = [
    url(r'^', include('movies.urls')),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]