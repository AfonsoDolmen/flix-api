from django.db import models
from django.core.validators import MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5, 'A avalição deve ser até 5 estrelas.'),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    
    def __str__(self) -> str:
        return self.movie.title
