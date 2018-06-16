from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Found_item(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    idNo = models.PositiveIntegerField()
    fullName = models.CharField(max_length=25)
    image = models.ImageField(upload_to='itemsFound/%Y/%m/%d', blank=True)
    dateFound = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.fullName
