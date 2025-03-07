# blog/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BlogCreateView, BlogDeleteView, BlogListView

urlpatterns = [
    # JWT Authentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Blog API Endpoints
    path('get/', BlogListView.as_view(), name='blog-api-list'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
]
