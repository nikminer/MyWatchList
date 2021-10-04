# Generated by Django 3.0.4 on 2021-08-30 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('MyWatchList', '0014_auto_20200411_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, default='users/default.png', upload_to='users')),
                ('sex', models.CharField(choices=[('M', 'Муж'), ('F', 'Жен')], default='1', max_length=1)),
                ('photobg', models.ImageField(blank=True, null=True, upload_to='users/bg')),
                ('following', models.ManyToManyField(related_name='followers', through='MyWatchList.Follower', to='MyWatchList.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sended', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('item_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('item_ct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_notifi', to='contenttypes.ContentType')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyWatchList.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sended', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('FromUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From', to='MyWatchList.Profile')),
                ('ToUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='To', to='MyWatchList.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Friendlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('accepter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link2', to='MyWatchList.Profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link1', to='MyWatchList.Profile')),
            ],
            managers=[
                ('friends', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='follower',
            name='follow_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to='MyWatchList.Profile'),
        ),
        migrations.AddField(
            model_name='follower',
            name='follow_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to='MyWatchList.Profile'),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('feed_type', models.CharField(max_length=20, null=True)),
                ('verb', models.CharField(max_length=255, null=True)),
                ('item_ct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_obj', to='contenttypes.ContentType')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyWatchList.Profile')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]