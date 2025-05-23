# Generated by Django 3.2.24 on 2024-06-21 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20240621_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='time',
        ),
        migrations.AddField(
            model_name='theory',
            name='time',
            field=models.IntegerField(default=10, verbose_name='Примерное время на прочтение статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 15, 44, 5, 433045), verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='articlefireworks',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 15, 44, 5, 434172), verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='calculatedtest',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 15, 44, 5, 440524), verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='test',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 21, 15, 44, 5, 438269), verbose_name='Дата и время публикации'),
        ),
    ]
