
from django.contrib import admin
from django.conf.urls import include, url
from .views import RegisterView, CustomLoginView


# urls
urlpatterns = [
    url(r'^', include('movies.urls')),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registration/', RegisterView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
]