# Generated by Django 3.2 on 2021-04-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinasiWisataYogyakarta', '0002_remove_destination_telephone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='images',
            new_name='image_url',
        ),
        migrations.AlterField(
            model_name='destination',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
