# Generated by Django 4.0.5 on 2022-06-05 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post/'),
        ),
    ]