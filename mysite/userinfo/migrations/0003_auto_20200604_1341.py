# Generated by Django 3.0.6 on 2020-06-04 05:41

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20200604_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfomodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='user'),
        ),
    ]
