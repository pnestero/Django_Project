from django.db import models

# Create your models here.


from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Имя продукта')
    description = models.TextField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='images/')
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')



    def __str__(self):
        return f'{self.product_name} {self.category_name} {self.description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name']
        db_table = 'product'



class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name']
        db_table = 'category'

