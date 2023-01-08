from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ModelForm(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(blank=True, verbose_name='Почта')
    phone = PhoneNumberField(region="RU", blank=True)
    date = models.DateField(null=True, blank=True, verbose_name='Дата')
    text = models.TextField(blank=True, verbose_name='Информация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


