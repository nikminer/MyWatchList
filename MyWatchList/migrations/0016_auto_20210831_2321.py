# Generated by Django 3.0.4 on 2021-08-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0015_auto_20210830_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='tmdbid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]