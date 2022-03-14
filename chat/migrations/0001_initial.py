# Generated by Django 3.2.9 on 2022-03-14 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date of create')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المنشئ')),
                ('invited', models.ManyToManyField(related_name='invited_user', to=settings.AUTH_USER_MODEL, verbose_name='غضو')),
            ],
            options={
                'verbose_name': 'chat room',
                'verbose_name_plural': 'chat room',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='text')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ المغادرة')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.room', verbose_name='chat room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'text chat',
                'verbose_name_plural': 'texts chat',
            },
        ),
    ]
