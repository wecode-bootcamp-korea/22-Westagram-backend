# Generated by Django 3.2.4 on 2021-06-24 22:37

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
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
