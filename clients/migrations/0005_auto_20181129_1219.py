# Generated by Django 2.1.3 on 2018-11-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20181129_1140'),
        ('clients', '0004_auto_20181129_1140'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='clientservices',
            unique_together={('client', 'service')},
        ),
    ]
