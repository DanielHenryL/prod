# Generated by Django 2.2 on 2022-04-26 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
    ]