# Generated by Django 2.2.12 on 2022-10-25 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='waktu_posting',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='barang',
            name='harga',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='barang',
            name='link_gbr',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='barang',
            name='nama',
            field=models.CharField(max_length=50),
        ),
    ]
