# Generated by Django 3.2 on 2021-05-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0017_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]