# Generated by Django 3.2.25 on 2024-04-07 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('age', models.CharField(blank=True, max_length=255)),
                ('breed', models.CharField(blank=True, max_length=255)),
                ('sex', models.CharField(blank=True, max_length=255)),
                ('children', models.CharField(blank=True, max_length=255)),
                ('other_animals', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_advert_xeejcr', upload_to='images/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
