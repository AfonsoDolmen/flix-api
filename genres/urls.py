from django.urls import path
from genres.views import GenreListCreateView, GenreRetriveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
