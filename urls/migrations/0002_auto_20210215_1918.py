# Generated by Django 3.1.4 on 2021-02-15 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('price_different', '-created')},
        ),
    ]
