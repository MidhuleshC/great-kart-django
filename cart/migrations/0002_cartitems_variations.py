# Generated by Django 4.0.4 on 2022-06-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_variation_variations'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variations'),
        ),
    ]
