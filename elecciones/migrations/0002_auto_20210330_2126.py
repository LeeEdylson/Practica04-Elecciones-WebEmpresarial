# Generated by Django 3.1.7 on 2021-03-31 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidato',
            old_name='candidato',
            new_name='candidato_name',
        ),
    ]
