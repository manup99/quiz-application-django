# Generated by Django 2.2.1 on 2019-06-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20190608_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='c',
        ),
        migrations.RemoveField(
            model_name='question',
            name='q_no',
        ),
        migrations.AddField(
            model_name='quiz',
            name='array',
            field=models.IntegerField(default=1),
        ),
    ]
