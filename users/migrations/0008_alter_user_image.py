# Generated by Django 4.2.17 on 2025-01-09 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_options_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='deps/images/baseavatar.jpg', null=True, upload_to='users/images', verbose_name='Аватар'),
        ),
    ]
