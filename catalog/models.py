from django.db import models

# Create your models here. Создание таблицы.


from django.db import models


class Product(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name="Имя продукта", help_text="Введите имя продукта"
    )
    description = models.TextField(
        max_length=300,
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="images_product/",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото",
    )
    category_name = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория",
        help_text="Введите описание продукта",
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["product_name"]
        db_table = "product"

    def __str__(self):
        return f"{self.product_name} {self.category_name} {self.description}"


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.TextField(max_length=150, verbose_name="Описание")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["category_name"]
        db_table = "category"

    def __str__(self):
        return f"{self.category_name} {self.description}"
