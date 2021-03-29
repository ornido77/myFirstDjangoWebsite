from django.db import models

# Create your models here.
class Names(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class notes(models.Model):
    name = models.ForeignKey(Names, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text