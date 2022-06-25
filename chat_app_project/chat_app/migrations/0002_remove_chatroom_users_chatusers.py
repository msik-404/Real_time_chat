# Generated by Django 4.0.5 on 2022-06-25 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='users',
        ),
        migrations.CreateModel(
            name='ChatUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chat_app.chatroom')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
