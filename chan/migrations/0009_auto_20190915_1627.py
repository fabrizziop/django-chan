# Generated by Django 2.2.5 on 2019-09-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chan', '0008_auto_20190915_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanpost',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
