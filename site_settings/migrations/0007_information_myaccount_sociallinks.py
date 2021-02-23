# Generated by Django 3.1.6 on 2021-02-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0006_auto_20210220_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MyAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us_short_cut', models.TextField(max_length=30)),
                ('instagram', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('pinterest', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
    ]