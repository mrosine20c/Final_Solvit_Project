# Generated by Django 4.1 on 2023-04-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangomodel',
            name='progress',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
