# Generated by Django 3.0.4 on 2021-08-31 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyWatchList', '0017_auto_20210831_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserListRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyWatchList.UserList')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyWatchList.Movie')),
            ],
            options={
                'unique_together': {('header', 'movie')},
            },
        ),
        migrations.DeleteModel(
            name='Friendlist',
        ),
    ]
