# Generated by Django 2.0 on 2017-12-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_agency', '0003_auto_20171213_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='desc',
            field=models.CharField(default='', max_length=255),
        ),
    ]
