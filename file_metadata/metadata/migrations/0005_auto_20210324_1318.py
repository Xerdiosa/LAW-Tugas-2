# Generated by Django 3.1.7 on 2021-03-24 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0004_auto_20210324_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadata',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='metadata',
            old_name='modified_date',
            new_name='modified_at',
        ),
    ]
