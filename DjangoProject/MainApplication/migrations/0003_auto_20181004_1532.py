# Generated by Django 2.0.3 on 2018-10-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApplication', '0002_auto_20181004_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userRollNumber',
            field=models.CharField(max_length=15),
        ),
    ]