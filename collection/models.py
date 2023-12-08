from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse


class Collection(models.Model):
    """ Модель коллекции, здесь используется отношения многие ко многим, поле bookmarks
    а так же связь с моделью django - User, для того чтобы у каждого пользователя
    были свои коллекции и закладки"""
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.CharField(verbose_name='Краткое описания', max_length=500)
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    bookmarks = models.ManyToManyField('Bookmark')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('collection', kwargs={'pk': self.pk})


class Bookmark(models.Model):
    """ Модель закладки, так же используется модель django - User """
    title = models.CharField(verbose_name='Название', max_length=255, default="Не найден")
    description = models.TextField(verbose_name='Краткое описания', max_length=3000, blank=True, default='Не найден')
    url = models.URLField(verbose_name='Ссылка')
    og_type = models.CharField(verbose_name='Тип Open Graph ссылки', max_length=255, default='website')
    og_image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото Open Graph', default='Не найден')
    site_name = models.CharField(verbose_name='Название сайта', max_length=255, default='Не найден')
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.url
    
    def get_absolute_url(self):
        return reverse('bookmark', kwargs={'pk': self.pk})