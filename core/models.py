# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models

# Create your models here.


class USER(models.Model):
	USER_ID = models.AutoField(primary_key=True)
	USER_NAME = models.CharField(max_length=32,unique=True)
	USER_PASSWORD = models.CharField(max_length=255)
	USER_FULLNAME = models.CharField(max_length=128)
	USER_BIRTHDAY = models.DateField()
	USER_EMAIL = models.EmailField(max_length=128,unique=True)
	USER_TELEPHONE = models.CharField(max_length=32)
	USER_MATRICULA = models.CharField(max_length=16)
	USER_DESCRIPTION = models.CharField(max_length=255)
	USER_CAMPUS = models.CharField(max_length=64,unique=True)
	def __srt__(self):
		return(self.USER_NAME)

class IMAGE(models.Model):
	IMAGES_ID = models.AutoField(primary_key=True)
	IMAGES_URL = models.ImageField()

class TAG(models.Model):
	TAG_ID = models.AutoField(primary_key=True)
	TAG_NAME = models.CharField(max_length=32)

class POST(models.Model):
	POST_ID = models.AutoField(primary_key=True)
	POST_USER = models.ForeignKey(USER)
	POST_BASE = models.ForeignKey('POST',null=True)
	POST_TITLE = models.CharField(max_length=128)
	POST_TEXT = models.TextField()
	POST_IMAGES = models.ManyToManyField(IMAGE,blank=True)
	POST_LOCAL = models.CharField(max_length=128)
	POST_TIME = models.DateTimeField(default=now)
	

	

class LOST(models.Model):
	LOST_ID = models.AutoField(primary_key=True)
	LOST_POST = models.ForeignKey(POST)
	LOST_USER = models.ForeignKey(USER)
	LOST_TIME = models.DateTimeField()
