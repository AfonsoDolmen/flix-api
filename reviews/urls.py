from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestoryView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestoryView.as_view(), name='reviews-detail-view'),
]

