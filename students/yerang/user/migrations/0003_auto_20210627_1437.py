# Generated by Django 3.2.4 on 2021-06-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0004_alter_comment_table'),
        ('user', '0002_auto_20210625_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postings.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='liked_posts',
            field=models.ManyToManyField(related_name='liked_users', through='user.Like', to='postings.Post'),
        ),
    ]
