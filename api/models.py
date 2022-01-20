from django.db import models
from django.contrib.auth.models import User


class contactmodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class uploadmodel(models.Model):
    writer = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="media")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args , **kwargs)


