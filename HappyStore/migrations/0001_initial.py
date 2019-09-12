# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-21 06:30
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetimefield', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('oonvan', models.CharField(max_length=20, verbose_name='عنوان پست')),
                ('matn', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن')),
                ('email', models.EmailField(max_length=254, verbose_name='ايميل نويسنده')),
                ('img', models.ImageField(upload_to='/Users/SAJIPY/Envs/KhoshhalStore/khoshhalistore/media', verbose_name='عکس')),
                ('price', models.CharField(max_length=20, verbose_name='قیمت محصول')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نويسنده')),
            ],
        ),
    ]