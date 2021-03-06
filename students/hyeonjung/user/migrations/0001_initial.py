# Generated by Django 3.2.4 on 2021-06-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
