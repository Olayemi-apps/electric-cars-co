# Generated by Django 3.2.4 on 2021-06-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='colour',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
