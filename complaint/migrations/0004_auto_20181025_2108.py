# Generated by Django 2.0.3 on 2018-10-25 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_sports'),
    ]

    operations = [
        migrations.CreateModel(
            name='latestOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggedInUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=45)),
                ('paword', models.CharField(max_length=45)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userRollNumber', models.IntegerField()),
                ('userFName', models.CharField(max_length=45)),
                ('userLName', models.CharField(max_length=45)),
                ('userMobileNumber', models.CharField(max_length=10)),
                ('UserUg', models.CharField(max_length=10)),
                ('UserMailId', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='academics',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.User'),
        ),
        migrations.AddField(
            model_name='login',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.User'),
        ),
        migrations.AddField(
            model_name='latestotp',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.User'),
        ),
    ]
