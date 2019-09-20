# Generated by Django 2.2.5 on 2019-09-14 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChanBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=300)),
                ('board_alias', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ChanPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.TextField()),
                ('post_content', models.TextField()),
                ('post_date', models.DateTimeField()),
                ('post_pw', models.CharField(max_length=128)),
                ('post_trip', models.CharField(max_length=128)),
                ('post_container_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chan.ChanBoard')),
            ],
        ),
        migrations.CreateModel(
            name='ChanPostReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_title', models.TextField()),
                ('reply_content', models.TextField()),
                ('reply_date', models.DateTimeField()),
                ('reply_pw', models.CharField(max_length=128)),
                ('reply_trip', models.CharField(max_length=128)),
                ('reply_container_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chan.ChanPost')),
            ],
        ),
    ]