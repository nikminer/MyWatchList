# Generated by Django 3.0.2 on 2020-01-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20191130_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='genrelist',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ('serial__name', 'name')},
        ),
        migrations.AlterModelOptions(
            name='serial',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='season',
            name='rating',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
