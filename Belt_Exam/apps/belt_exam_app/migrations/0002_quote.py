# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', models.TextField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes_posted', to='belt_exam_app.User')),
                ('favourites', models.ManyToManyField(related_name='favourite_quotes', to='belt_exam_app.User')),
            ],
        ),
    ]
