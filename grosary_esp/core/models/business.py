from django.db import models
from .base_model import BaseModel
from django.contrib.auth.models import User

class BusinessType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
