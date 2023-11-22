# Generated by Django 4.2.7 on 2023-11-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='изображение')),
                ('category', models.CharField(max_length=50, verbose_name='категория')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='цена за покупку')),
                ('date_of_creation', models.DateTimeField(blank=True, null=True, verbose_name='дата создания')),
                ('last_modified_date', models.DateTimeField(blank=True, null=True, verbose_name='дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
