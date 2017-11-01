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
class Web(models.Model):
    name_of_page = models.CharField(max_length=50, default='Главная страница и общая информация')
    phone = models.CharField(max_length=20, default='+7 (495) 968 77 43')
    email = models.CharField(max_length=30, default='ae@presscorp.ru')
    adress = models.CharField(max_length=150, default='г. Москва, ул. Нагатинская, 3а')
    vk = models.CharField(max_length=100, default='https://vk.com/presscorp')
    fb = models.CharField(max_length=100, default='https://www.facebook.com/PressCorp/')
    insta = models.CharField(max_length=100, default='https://www.instagram.com/presscorp/')

    class Meta:
        verbose_name = ("Главная страница")
        verbose_name_plural = ("Главная страница")

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name_of_page) or u''