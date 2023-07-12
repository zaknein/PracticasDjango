# Generated by Django 4.2 on 2023-07-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_descripcion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField(default=20)),
            ],
        ),
    ]
