from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    # author is a link to another table
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # title is a char field
    title = models.CharField(max_length=200)
    # text is a text field
    text = models.TextField()
    # created date is date field
    created_date = models.DateTimeField(default=timezone.now)
    # published date is date time field
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
