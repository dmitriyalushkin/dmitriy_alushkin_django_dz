# Generated by Django 4.2.7 on 2023-11-28 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_blogentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'verbose_name': 'блоговая запись', 'verbose_name_plural': 'блоговые записи'},
        ),
    ]
