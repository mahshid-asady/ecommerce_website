# Generated by Django 3.1.6 on 2021-02-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='title',
            field=models.CharField(default=11, max_length=30),
            preserve_default=False,
        ),
    ]
