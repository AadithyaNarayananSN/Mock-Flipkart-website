# Generated by Django 4.1.5 on 2023-01-03 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flipapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regmodel',
            old_name='companyname',
            new_name='name',
        ),
    ]
