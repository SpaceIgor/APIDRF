from django.db import models


class Direction(models.Model):
    name_direction = models.CharField('Назва напрямку', max_length=200)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='Слаг')


    class Meta:
        verbose_name = 'Напрямок'
        verbose_name_plural = 'Напрямки'

    def __str__(self):
        return self.name_direction


class Doctor(models.Model):
    name_doctor = models.CharField('ПІБ', max_length=200)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='Слаг')
    direction = models.ManyToManyField(Direction, verbose_name='Напрямок', related_name='direction',)
    description = models.TextField('Опис')
    date_of_birth = models.DateField('Дата народження', auto_now_add=False)
    experience = models.DecimalField('Досвід роботи', max_digits=5, decimal_places=1)


    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'

    def __str__(self):
        return self.name_doctor
