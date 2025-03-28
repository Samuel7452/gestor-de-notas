from django.urls import path
from .functions import create_category
from .views import CategoriesAPIView,CategoryDeleteView

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view(), name='category-create'),
    path('categories/new/', create_category, name='create_category'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
