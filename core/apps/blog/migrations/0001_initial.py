# Generated by Django 5.0 on 2023-12-21 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/Blog')),
                ('content', models.TextField()),
                ('tags', models.CharField(max_length=100, null=True)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
