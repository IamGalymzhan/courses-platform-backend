# Generated by Django 5.1.4 on 2024-12-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_lesson_quiz_data_lesson_quiz_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='quiz_file',
        ),
        migrations.AddField(
            model_name='lesson',
            name='quiz',
            field=models.JSONField(blank=True, null=True),
        ),
    ]