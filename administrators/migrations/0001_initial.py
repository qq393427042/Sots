# Generated by Django 2.0.1 on 2018-02-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobName', models.CharField(max_length=30)),
                ('JobPlace', models.CharField(max_length=10)),
                ('JobSalary', models.CharField(max_length=10)),
                ('JobAdvantage', models.CharField(max_length=30)),
                ('releaseTime', models.CharField(max_length=30)),
                ('jobNeed', models.CharField(max_length=30)),
                ('educationRequire', models.CharField(max_length=30)),
                ('experienceRequire', models.CharField(max_length=30)),
                ('skillRequire', models.CharField(max_length=30)),
                ('jobLink', models.CharField(max_length=200)),
                ('jobInfo', models.TextField()),
                ('jobNature', models.CharField(max_length=20)),
                ('jobLabels', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=10)),
            ],
        ),
    ]
