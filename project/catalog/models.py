from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)


    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='дата последнего изменения', **NULLABLE)


    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class BlogEntry(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='символы')
    content = models.TextField(verbose_name='содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog_entry/', verbose_name='изображение',
                              **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=False,
                                            verbose_name='дата создания', **NULLABLE)
    sign_of_publication = models.BooleanField(default=True,
                                              verbose_name='признак публикации',
                                              **NULLABLE)
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров', **NULLABLE)


    def __str__(self):
        return f'{self.header}'


    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'