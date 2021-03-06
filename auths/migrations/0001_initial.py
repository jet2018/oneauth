# Generated by Django 3.2.9 on 2021-11-20 19:42

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
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('secondary_phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('latitude', models.CharField(blank=True, max_length=100)),
                ('longitude', models.CharField(blank=True, max_length=100)),
                ('profession', models.CharField(blank=True, max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=4)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('youtube', models.CharField(blank=True, max_length=100)),
                ('github', models.CharField(blank=True, max_length=100)),
                ('google', models.CharField(blank=True, max_length=100)),
                ('snapchat', models.CharField(blank=True, max_length=100)),
                ('tumblr', models.CharField(blank=True, max_length=100)),
                ('pinterest', models.CharField(blank=True, max_length=100)),
                ('reddit', models.CharField(blank=True, max_length=100)),
                ('vimeo', models.CharField(blank=True, max_length=100)),
                ('twitch', models.CharField(blank=True, max_length=100)),
                ('soundcloud', models.CharField(blank=True, max_length=100)),
                ('whatsapp', models.CharField(blank=True, max_length=100)),
                ('telegram', models.CharField(blank=True, max_length=100)),
                ('skype', models.CharField(blank=True, max_length=100)),
                ('stack_over_flow', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
