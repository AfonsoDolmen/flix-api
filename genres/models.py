from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Gêneros')


    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self) -> str:
        return self.name
