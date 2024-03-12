
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('api/roran-williams/blogs/', include('blogs.urls')),
    path('api/roran-williams/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]