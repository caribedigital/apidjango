# Generated by Django 4.0 on 2021-12-29 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apicursos',
            old_name='lenguaje',
            new_name='language',
        ),
    ]
