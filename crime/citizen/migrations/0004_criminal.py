# Generated by Django 2.2.6 on 2019-11-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0003_theft'),
    ]

    operations = [
        migrations.CreateModel(
            name='criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('cname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('remarks', models.CharField(max_length=250)),
                ('cid', models.IntegerField()),
            ],
        ),
    ]
