# Generated by Django 2.0.3 on 2018-10-25 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_auto_20181026_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventId', models.AutoField(primary_key=True, serialize=False)),
                ('subcatId', models.IntegerField()),
                ('eventname', models.CharField(max_length=45)),
                ('fromdate', models.DateTimeField()),
                ('todate', models.DateTimeField()),
                ('nature', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=400)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.User')),
            ],
        ),
    ]
