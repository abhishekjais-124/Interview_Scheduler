# Generated by Django 3.2.4 on 2021-06-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='emails',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='interviews',
            name='email',
        ),
        migrations.AddField(
            model_name='interviews',
            name='emails',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
