# Generated by Django 2.2 on 2021-04-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='description',
            field=models.TextField(max_length=1540),
        ),
    ]
