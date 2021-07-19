# Generated by Django 3.1.6 on 2021-07-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['posted_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='posted',
            new_name='posted_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='edited',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=None, max_length=80),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
