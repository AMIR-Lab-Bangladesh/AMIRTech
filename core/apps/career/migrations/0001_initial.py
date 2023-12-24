# Generated by Django 5.0 on 2023-12-22 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('designation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255, null=True)),
                ('location', models.BooleanField(null=True)),
                ('salary', models.FloatField(null=True)),
                ('description', models.TextField(null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='career/thumbnail')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='career_designation', to='designation.designation')),
            ],
        ),
    ]