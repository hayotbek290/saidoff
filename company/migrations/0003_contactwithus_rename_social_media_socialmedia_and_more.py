# Generated by Django 5.0.7 on 2024-07-15 14:22

import company.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_social_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactWithUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100, validators=[company.validators.validate_phone_number])),
                ('massage', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact With Us',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.RenameModel(
            old_name='Social_media',
            new_name='SocialMedia',
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]