from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    # use FileField for any other files

    def __str__(self):
        return self.title
