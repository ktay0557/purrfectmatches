# Generated by Django 3.2.25 on 2024-04-27 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoption',
            old_name='advert',
            new_name='advert_id',
        ),
    ]