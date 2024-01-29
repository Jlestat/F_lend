from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='Название новости', max_length=255)
    content = models.TextField(verbose_name='Содержание новости')
    published_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
