# Generated by Django 4.0.3 on 2022-03-13 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Heroes',
            new_name='Hero',
        ),
    ]
