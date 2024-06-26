# Generated by Django 3.2.25 on 2024-04-06 15:37

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=11)),
                ('location', models.TextField(blank=True)),
                ('previously_owned', models.CharField(blank=True, max_length=255)),
                ('currently_own', models.TextField(blank=True)),
                ('relationship_status', models.CharField(blank=True, max_length=255)),
                ('children', models.CharField(blank=True, max_length=255)),
                ('housing', models.CharField(blank=True, max_length=255)),
                ('hobbies', models.TextField(blank=True)),
                ('preferred_breed', models.CharField(blank=True, max_length=255)),
                ('preferred_age', models.CharField(blank=True, max_length=255)),
                ('preferred_sex', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(default='../default_profile_htuvfk', upload_to='images/')),
                ('is_staff', models.BooleanField(default=False)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
