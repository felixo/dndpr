#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Slider(models.Model):
    number = models.IntegerField(default=0)
    img = models.FileField(upload_to='media/slider')
    link = models.CharField(max_length=100, default='/')
    name = models.CharField(max_length=50, default='Слайдер №')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''
# Create your models here.
