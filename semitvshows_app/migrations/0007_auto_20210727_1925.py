# Generated by Django 2.2 on 2021-07-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semitvshows_app', '0006_auto_20210727_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
