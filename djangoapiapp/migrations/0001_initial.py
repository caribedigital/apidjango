# Generated by Django 4.0 on 2021-12-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apicursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lenguaje', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
