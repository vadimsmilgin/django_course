from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, blank=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __srt__(self):
        return str(self.name)
        pass


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назвение")
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.FloatField(db_index=True, blank=True, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'name', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __srt__(self):
        return str(self.name)
        pass

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})