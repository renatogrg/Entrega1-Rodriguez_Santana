# Generated by Django 4.2 on 2023-05-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionextra',
            name='descripcion',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
