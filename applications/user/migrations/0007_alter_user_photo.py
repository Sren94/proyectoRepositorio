# Generated by Django 5.0.6 on 2024-05-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/<django.db.models.fields.CharField>/', verbose_name='Fotografia'),
        ),
    ]
