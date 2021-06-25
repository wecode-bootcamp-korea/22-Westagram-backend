# Generated by Django 3.2.4 on 2021-06-25 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_nmber', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('full_name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('nick_name', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('login_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
