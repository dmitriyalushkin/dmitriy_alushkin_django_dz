# Generated by Django 4.2.7 on 2023-11-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='символы')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_entry/', verbose_name='изображение')),
                ('date_of_creation', models.DateTimeField(blank=True, null=True, verbose_name='дата создания')),
                ('sign_of_publication', models.BooleanField(blank=True, null=True, verbose_name='признак публикации')),
                ('number_of_views', models.IntegerField(blank=True, null=True, verbose_name='количество просмотров')),
            ],
        ),
    ]