from django.db import models


# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=234)

    def __str__(self):
        return self.name


class Cards(models.Model):
    name = models.ForeignKey(About, on_delete=models.CASCADE)
    trainer = models.CharField(max_length=234)
    image = models.CharField(max_length=3000)
