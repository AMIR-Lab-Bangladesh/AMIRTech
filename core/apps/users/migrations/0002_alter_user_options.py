# Generated by Django 5.0 on 2023-12-21 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id'], 'verbose_name_plural': 'Custom Users'},
        ),
    ]
