# Generated by Django 2.0.7 on 2018-07-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20180723_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sponser',
            field=models.ManyToManyField(blank=True, to='sponser.Sponser'),
        ),
    ]