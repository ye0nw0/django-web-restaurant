# Generated by Django 4.0 on 2021-12-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webthird', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='password',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
