# Generated by Django 2.2.5 on 2019-09-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0002_auto_20190914_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanpost',
            name='post_content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='chanpost',
            name='post_img',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpost',
            name='post_ip',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpost',
            name='post_pw',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpost',
            name='post_title',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='chanpost',
            name='post_trip',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_img',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_ip',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_pw',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_title',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='chanpostreply',
            name='reply_trip',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
