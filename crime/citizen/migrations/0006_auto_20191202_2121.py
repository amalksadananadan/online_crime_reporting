# Generated by Django 2.2.1 on 2019-12-02 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0005_citizenreg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='cid',
            new_name='ctid',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='disid',
        ),
    ]
