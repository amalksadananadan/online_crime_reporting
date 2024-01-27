# Generated by Django 2.2.6 on 2019-11-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lawyerreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('hname', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('photo', models.FileField(upload_to='file')),
                ('qual', models.FileField(upload_to='file')),
                ('proof', models.FileField(upload_to='file')),
                ('uname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
