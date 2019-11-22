# Generated by Django 2.2.5 on 2019-11-21 14:03

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
            name='User_data',
            fields=[
                ('Admission_Number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Father_name', models.CharField(max_length=40)),
                ('profile_pic', models.ImageField(blank=True, upload_to='user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
