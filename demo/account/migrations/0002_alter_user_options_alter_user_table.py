# Generated by Django 5.0.6 on 2024-07-23 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'userinfo'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
