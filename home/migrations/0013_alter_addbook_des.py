# Generated by Django 3.2.4 on 2021-09-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_addbook_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='des',
            field=models.TextField(max_length=200),
        ),
    ]
