# Generated by Django 3.2.4 on 2021-09-01 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210901_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addbook',
            old_name='book',
            new_name='student',
        ),
    ]
