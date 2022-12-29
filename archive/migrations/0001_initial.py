# Generated by Django 4.1 on 2022-08-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mail', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('sender', models.CharField(max_length=200)),
                ('regarding', models.CharField(max_length=100)),
                ('file_or_image', models.FileField(upload_to='storage/incoming-mail/')),
            ],
        ),
        migrations.CreateModel(
            name='OutgoingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mail', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('to_send', models.CharField(max_length=100)),
                ('regarding', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('file_or_image', models.FileField(upload_to='storage/outgoing-mail/')),
            ],
        ),
    ]