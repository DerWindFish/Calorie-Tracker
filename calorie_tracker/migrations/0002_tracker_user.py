# Generated by Django 4.1.1 on 2022-09-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
    ]
