# Generated by Django 3.2.4 on 2021-06-25 11:19

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
                ('nick_name', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100, null=True)),
                ('bio', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('custom', 'Custom'), ('prefer not to say', 'Prefer Not To Say')], max_length=20, verbose_name='Gender')),
                ('birth_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
