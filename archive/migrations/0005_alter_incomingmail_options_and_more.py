# Generated by Django 4.1 on 2022-09-07 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_alter_incomingmail_file_or_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomingmail',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='outgoingmail',
            options={'ordering': ('-id',)},
        ),
    ]
