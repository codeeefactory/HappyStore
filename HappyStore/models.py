# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.

class POST(models.Model):
	writer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('نويسنده'), null=True)
	createDateTime = models.DateTimeField(_('create date'), auto_now_add=True, auto_now=False)
	updateDateTime = models.DateTimeField(_('update date'), auto_now_add=False, auto_now=True)

	oonvan=models.CharField(_('عنوان پست'),max_length=20)
	matn=RichTextUploadingField(_('توضیحات'), config_name='default')
	img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	price = models.CharField(_("قیمت محصول"),max_length=20)
	def __unicode__():
		return self.oonvan+"<br>"+self.matn+"<br><br>"
class Products(models.Model):
	prod1 =	models.CharField(_('نام محصول'),max_length=20)
	prod1_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod1_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod2 =	models.CharField(_('2نام محصول'),max_length=20)
	prod2_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod2_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod3 =	models.CharField(_('3نام محصول'),max_length=20)
	prod3_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod3_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod4 =	models.CharField(_('4نام محصول'),max_length=20)
	prod4_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod4_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod5 =	models.CharField(_('5نام محصول'),max_length=20)
	prod5_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod5_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod6 =	models.CharField(_('6نام محصول'),max_length=20)
	prod6_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod6_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod7 =	models.CharField(_('7نام محصول'),max_length=20)
	prod7_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod7_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod8 =	models.CharField(_('8نام محصول'),max_length=20)
	prod8_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod8_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod9 =	models.CharField(_('9نام محصول'),max_length=20)
	prod9_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod9_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	prod10 =	models.CharField(_('10نام محصول'),max_length=20)
	prod10_info=RichTextUploadingField(_('توضیحات'), config_name='default')
	prod10_img = models.ImageField("عکس",upload_to="/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media")
	def __unicode__():
		return self.prod1+"<br>"+self.matn+"<br><br>"