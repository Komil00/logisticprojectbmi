# Generated by Django 4.2 on 2023-04-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartransport',
            name='route',
            field=models.CharField(max_length=300),
        ),
    ]
