# Generated by Django 3.0.3 on 2020-05-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_submission_text_file_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='programming_language',
            field=models.CharField(default='Python', max_length=255, verbose_name='Programming language name'),
            preserve_default=False,
        ),
    ]