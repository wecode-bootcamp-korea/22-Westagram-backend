# Generated by Django 3.2.4 on 2021-06-27 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('postings', '0002_auto_20210626_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLikeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postings.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'comments_like_users',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_comment', through='postings.CommentLikeUser', to='user.User'),
        ),
    ]
