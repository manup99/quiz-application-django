# Generated by Django 2.2.1 on 2019-06-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20190608_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='array',
            field=models.IntegerField(default=0),
        ),
    ]
