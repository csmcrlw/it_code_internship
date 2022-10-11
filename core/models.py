import datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='items')
    name = models.CharField('Название', max_length=255, blank=True, unique=True)    # unique не разрешает делать записи с одинаковым значением поля name
    description = models.TextField('Описание', help_text='подсказка, если применимо')    # help_text оставляет "подсказку"
    priority = models.IntegerField('Приоритет сортировки', default=1, db_index=True)    # приоритет
    # done = models.BooleanField('Выполнено') лучше использовать:
    done = models.DateTimeField('Выполнено', null=True, blank=True)
    created = models.DateTimeField('Создано', auto_now_add=True, db_index=True)
    update = models.DateTimeField('Обновлено', auto_now=True)
    deleted = models.DateTimeField('время удаления', null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Метки', blank=True, related_name='items')    # related_name связывает одну таблицу с другой по переданному ключу

    """Класс Meta отвечает за добавление доп.информации к объекту класса Item"""
    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Список дел'
        ordering = ('priority', 'created')   # сортировка по полям priority и created, чтобы выполнялась быстрее, можно проиндексировать поля через db_index=True

    def __str__(self):
        return self.name

    def duration(self) -> datetime.timedelta:
        """Метод, позволяющий определить, как давно был создан объект"""
        return now() - self.created

    """В методах не нужно создавать бизнес-логику!"""
