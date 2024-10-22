from django.core.validators import MinLengthValidator
from django.db import models

from music_project.profiles.validators import AlfaNumericUnderscoreValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlfaNumericUnderscoreValidator(),
        ],
    )
    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


