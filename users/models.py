from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class items_found(models.Model):
    user = models.OneToOneField(User)
    idNo = models.PositiveIntegerField()
    fullName = models.CharField(max_length=25)
    image = models.ImageField(upload_to='itemsFound/%Y/%m/%d', blank=True)
    dateFound = models.DateTimeField(auto_now=False)

    