# Generated by Django 4.0.4 on 2022-06-05 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]