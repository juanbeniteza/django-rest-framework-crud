from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateBlogAPIView.as_view(), name='get_post_blogs'),
    path('<int:pk>/', views.RetrieveUpdateDestroyBlogAPIView.as_view(), name='get_delete_update_blog'),
]