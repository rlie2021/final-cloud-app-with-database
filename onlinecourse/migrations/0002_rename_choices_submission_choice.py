# Generated by Django 4.0.4 on 2022-05-15 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='choices',
            new_name='choice',
        ),
    ]