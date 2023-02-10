from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    '''User with minimal requirments,rest of the field provided by abstract class'''
    username = models.EmailField(_('email as usename'),unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.email = self.username
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    

class RequestCounter(models.Model):
    '''This model store request counts concurrently'''
    counts = models.BigIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.counts