# Generated by Django 2.0 on 2018-01-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstraction',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
