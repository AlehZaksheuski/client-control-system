# Generated by Django 2.1.3 on 2018-11-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20181129_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientservices',
            name='service_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания услуги'),
        ),
        migrations.AddField(
            model_name='clientservices',
            name='service_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата активации услуги'),
        ),
    ]
