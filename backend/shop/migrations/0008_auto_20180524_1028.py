# Generated by Django 2.0.5 on 2018-05-24 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='titel',
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
