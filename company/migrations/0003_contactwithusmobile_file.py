# Generated by Django 5.0.7 on 2024-07-29 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('company', '0002_appinfo_contactwithuscategory_contactwithusmobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactwithusmobile',
            name='file',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.media'),
            preserve_default=False,
        ),
    ]
