# Generated by Django 2.2.1 on 2019-06-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
