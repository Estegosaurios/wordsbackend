from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    tags = models.ManyToManyField(Tag, related_name='words')

    def __str__(self):
        return self.name
