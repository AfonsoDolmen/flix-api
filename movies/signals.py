from django.db.models.signals import pre_save
from django.dispatch import receiver
from movies.models import Movie
from movies.utils import openai_api


@receiver(pre_save, sender=Movie)
def generate_resume_pre_save(sender, instance, **kwargs):
    if not instance.resume:
        instance.resume = openai_api.generate_resume(
            instance.title,
            instance.genre,
            instance.release_date
        )
