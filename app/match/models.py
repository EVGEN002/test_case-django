from django.db import models

# Create your models here.

from django.urls import reverse

class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender

class Match(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.second_name} {self.id}'

    def get_absolute_url(self):
        return reverse('human', args=[str(self.id)])