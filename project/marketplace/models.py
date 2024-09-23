from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Mango(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    variety = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    images = models.ImageField(upload_to='mangoes/')
    video = models.URLField(blank=True, null=True)
    taste_review = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.variety

class TreeDetails(models.Model):
    mango = models.OneToOneField(Mango, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)  # Ensure this field exists
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    variety = models.CharField(max_length=100)
    fertilizer_used = models.TextField(blank=True, null=True)
    tree_images = models.ImageField(upload_to='trees/', blank=True, null=True)
    pesticide_used = models.BooleanField(default=False)
    tree_video = models.URLField(blank=True, null=True)


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    mango = models.ForeignKey(Mango, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.buyer.username}"

# marketplace/models.py

from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Mango)
def delete_mango_files(sender, instance, **kwargs):
    if instance.images:
        instance.images.delete(False)

