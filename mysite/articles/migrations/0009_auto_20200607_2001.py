# Generated by Django 3.0.6 on 2020-06-07 12:01

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_tagmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=50, unique=True)),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='tagname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
