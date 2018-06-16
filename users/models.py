
from django.db import models
from random import choice
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    surname = models.CharField(_('SurName'), max_length=50, blank=True, null=True)
    idno = models.PositiveIntegerField()
    phoneNo = models.PositiveIntegerField()

def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    