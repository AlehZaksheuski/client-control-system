# Generated by Django 2.1.3 on 2018-12-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20181129_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.TextField(verbose_name='Имя услуги'),
        ),
    ]
