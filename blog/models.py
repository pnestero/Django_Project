from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(default='', verbose_name='Содержимое')
    image = models.ImageField(upload_to="images_blog/", blank=True, null=True, verbose_name='Фотография')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_attribute = models.BooleanField(default=True, verbose_name='Признак публикации')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'blog_post'

    def __str__(self):
        return f"{self.title} {self.creation_date}"
