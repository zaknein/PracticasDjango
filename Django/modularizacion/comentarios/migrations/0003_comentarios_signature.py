# Generated by Django 4.2 on 2023-05-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comentarios_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]
