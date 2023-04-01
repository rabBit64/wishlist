from django.db import models

class WishList(models.Model):
    name  = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    date = models.DateField()