# Generated by Django 3.0.3 on 2020-05-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_exercise_text_file_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='text_file_content',
            field=models.TextField(blank=True, verbose_name='file.txt tab content'),
        ),
    ]