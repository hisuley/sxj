from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u' %s %s %s' % (self.title, self.body, self.timestamp)

    class Meta:
        ordering = ['-timestamp']