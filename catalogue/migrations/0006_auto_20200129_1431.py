# Generated by Django 2.2 on 2020-01-29 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20200129_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.PositiveIntegerField(),
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Purchase')),
            ],
        ),
    ]