# Generated by Django 2.2 on 2020-01-29 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20200129_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='count',
            new_name='total_cost',
        ),
    ]
