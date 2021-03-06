# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-04 17:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20180704_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puntaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='puntaje',
        ),
        migrations.AddField(
            model_name='puntaje',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Noticias'),
        ),
    ]
