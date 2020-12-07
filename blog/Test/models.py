from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name='Название группы', max_length=30)
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text_public = models.TextField(verbose_name='Текст публикации')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, related_name='Test')
    group = models.ForeignKey(Group, verbose_name='Группа', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}:{}".format(self.author, self.text_public)

