# Generated by Django 3.2.4 on 2021-06-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salesexecutive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('best_sales_person', models.BooleanField(default=False)),
            ],
        ),
    ]
