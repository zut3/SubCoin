from django.db import models


class Price(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    updated = models.DateField(auto_now=True)


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
