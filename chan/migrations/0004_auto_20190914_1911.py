# Generated by Django 2.2.5 on 2019-09-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0003_auto_20190914_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanpost',
            name='post_img',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_img',
            field=models.FileField(upload_to=''),
        ),
    ]
