# Generated by Django 4.0.4 on 2022-06-05 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='auth',
        ),
    ]