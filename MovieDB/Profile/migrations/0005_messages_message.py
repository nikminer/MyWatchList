# Generated by Django 2.2.4 on 2019-12-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_messages_sended'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]