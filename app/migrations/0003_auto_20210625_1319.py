# Generated by Django 3.2.4 on 2021-06-25 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210625_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviews',
            name='emails',
        ),
        migrations.RemoveField(
            model_name='users',
            name='interviews',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
        migrations.AddField(
            model_name='interviews',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.users'),
            preserve_default=False,
        ),
    ]
