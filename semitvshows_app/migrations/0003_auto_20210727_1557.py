# Generated by Django 2.2 on 2021-07-27 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semitvshows_app', '0002_auto_20210727_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
