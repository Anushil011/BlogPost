# Generated by Django 3.2.8 on 2021-10-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_description_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image', upload_to='images'),
            preserve_default=False,
        ),
    ]
