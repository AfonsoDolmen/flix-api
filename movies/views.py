from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import response
from django.db.models import Count, Avg
from movies.serializers import MovieSerializer
from movies.models import Movie
from reviews.models import Review
from app.permissions import GlobalDefaultPermission


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        # Busca todos os dados
        total_movies = self.queryset.count()
        total_movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        reviews_average = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response({
            'total_movies': total_movies,
            'total_movies_by_genre': total_movies_by_genre,
            'total_reviews': total_reviews,
            'reviews_average': reviews_average,
        },status.HTTP_200_OK)
