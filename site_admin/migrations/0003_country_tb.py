# Generated by Django 3.2.8 on 2022-02-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0002_image_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='country_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]
