# Generated by Django 3.1.4 on 2020-12-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201222_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
