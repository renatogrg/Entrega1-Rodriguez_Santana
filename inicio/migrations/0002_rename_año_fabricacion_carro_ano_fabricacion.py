# Generated by Django 4.2 on 2023-05-01 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='año_fabricacion',
            new_name='ano_fabricacion',
        ),
    ]
