# Generated by Django 4.2.1 on 2023-07-01 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misapp', '0005_alter_articulos_options_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='CustomUser',
            options={'verbose_name': 'CustomUser', 'verbose_name_plural': 'CustomsUsers'},
        ),
        migrations.AlterModelTable(
            name='CustomUser',
            table='CustomUser',
        ),
    ]
