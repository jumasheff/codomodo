# Generated by Django 4.1.4 on 2022-12-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_submission_hint_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='output',
            field=models.TextField(blank=True, verbose_name='Result'),
        ),
    ]
