# Generated by Django 3.2.4 on 2024-10-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_twcgma', upload_to='images/'),
        ),
    ]
