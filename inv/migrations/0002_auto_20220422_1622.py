# Generated by Django 2.2 on 2022-04-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la Categoría', max_length=100, unique=True),
        ),
    ]