# Generated by Django 5.2.2 on 2025-07-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_and_re', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
