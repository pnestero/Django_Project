from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория")
    description = models.TextField(max_length=150, verbose_name="Описание")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
        db_table = "category"

    def __str__(self):
        return f"{self.name} {self.description}"


class Product(models.Model):
    name = models.CharField(
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
    # Поле связи (внешний ключ)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория",
        help_text="Выберите категорию продукта",
        related_name="products",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        db_table = "catalog"

    def __str__(self):
        return f"{self.name} ({self.category})"