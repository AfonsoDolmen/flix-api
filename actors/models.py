from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        null=True,
        blank=True
    )


    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'

    def __str__(self) -> str:
        return self.name
