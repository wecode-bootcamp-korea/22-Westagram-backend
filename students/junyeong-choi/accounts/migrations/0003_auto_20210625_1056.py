# Generated by Django 3.2.4 on 2021-06-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210625_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='nickname',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
