# Generated by Django 3.1.3 on 2020-12-07 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20201202_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criterio',
            name='user',
        ),
    ]
