# Generated by Django 2.0.3 on 2018-10-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApplication', '0015_auto_20181024_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedInUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
            ],
        ),
    ]