from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __unicode__(self):
        return self.username