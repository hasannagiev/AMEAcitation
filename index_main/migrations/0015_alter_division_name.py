# Generated by Django 4.2.11 on 2024-04-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_main', '0014_profile_profileupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(default='Reyasət Heyəti', max_length=100),
        ),
    ]