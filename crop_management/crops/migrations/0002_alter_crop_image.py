# Generated by Django 5.0.1 on 2024-01-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='crops/images'),
        ),
    ]