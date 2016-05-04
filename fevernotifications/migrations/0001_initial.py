# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, db_index=True, max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
                ('target_id', models.PositiveIntegerField(null=True, verbose_name='related object')),
                ('status', models.CharField(choices=[('U', 'Unread'), ('R', 'Read'), ('D', 'Deleted')], db_index=True, default='U', max_length=50)),
                ('url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('expiration', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='target object')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
