# Generated by Django 3.1.4 on 2020-12-22 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
