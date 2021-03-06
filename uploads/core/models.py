from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class MyImage(models.Model):
    name = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    value = float
