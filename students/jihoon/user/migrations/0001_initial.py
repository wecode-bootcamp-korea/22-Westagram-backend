# Generated by Django 3.2.4 on 2021-06-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]