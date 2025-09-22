# ads/models.py

from django.db import models
from django.urls import reverse

class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    short_description = models.TextField(max_length=500, verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Полное описание")
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-publication_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('advertisement_detail', args=[str(self.id)])