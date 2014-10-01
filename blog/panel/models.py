from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def checkPass(self, username, password):

        try:
            theuser = User.objects.get(username=username)
            if theuser.password == password:
                return 1
            else:
                return 2
        except ObjectDoesNotExist:
            return 0

    def __unicode__(self):
        return self.username