# Generated by Django 2.0.5 on 2018-05-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='form',
            name='name',
            field=models.CharField(default='My form', max_length=300),
        ),
    ]
