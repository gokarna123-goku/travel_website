# Generated by Django 3.0.5 on 2021-04-10 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20210410_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='exipiry_date',
            new_name='expiry_date',
        ),
    ]