# Generated by Django 2.2.5 on 2019-09-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0013_auto_20190917_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='chan_images/'),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='image',
            field=models.ImageField(blank=True, upload_to='chan_images/'),
        ),
    ]
