# Generated by Django 5.0 on 2023-12-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100, null=True)),
                ('degree', models.CharField(max_length=100, null=True)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
            ],
        ),
    ]
