# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=15)),
                ('source', models.CharField(max_length=150)),
                ('order', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asin', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('manufacturer', models.CharField(max_length=150, null=True)),
                ('url', models.CharField(max_length=255)),
                ('catalog', models.ForeignKey(related_name='items', to='catalog.Catalog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
