# Generated by Django 4.2.8 on 2023-12-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default=1233, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='username',
            field=models.CharField(default=3445, max_length=100),
            preserve_default=False,
        ),
    ]
