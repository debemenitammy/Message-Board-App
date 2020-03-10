# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()


    def __str__(self):
        return self.text[:50]