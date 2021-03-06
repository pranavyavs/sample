# Generated by Django 3.2.8 on 2022-02-25 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0004_state_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='place_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=20)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.country_tb')),
                ('stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_admin.state_tb')),
            ],
        ),
    ]
