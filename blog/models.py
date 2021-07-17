from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='parent', blank=True, null=True,
                                  default=None)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='articles',
                                 on_delete=models.CASCADE,
                                 )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название статьи')
    image = models.ImageField(upload_to='images/', default='no_image_r619a3.jpg', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        index_together = ('id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])
