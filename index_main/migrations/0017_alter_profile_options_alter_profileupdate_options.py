# Generated by Django 5.0.4 on 2024-04-26 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_main', '0016_alter_profile_platform_alter_profile_profile_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profillər'},
        ),
        migrations.AlterModelOptions(
            name='profileupdate',
            options={'verbose_name': 'Profil məlumatı', 'verbose_name_plural': 'Profil məlumatları'},
        ),
    ]
