from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):


    def __str__(self):
        return self.name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Correct field name here



def get_absolute_url(self):
    return reverse('item-detail', kwargs={'pk': self.pk})

