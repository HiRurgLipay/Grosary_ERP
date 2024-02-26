from django.db import models

from .base_model import BaseModel


class Question(BaseModel):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
