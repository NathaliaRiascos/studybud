# Generated by Django 5.0.1 on 2024-01-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
