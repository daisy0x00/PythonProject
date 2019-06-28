# coding:utf-8

from django.db import models

# Create your models here.
class Genre(models.Model):
    """

    定义模型类
    有一个数据表，就有一个模型类与之对应
    模型类继承自models.Model类
    说明：不需要定义主键列，在生成时会自动添加，并且值为自动增长
    当输出对象时，会调用对象的str方法
    自动生成的表名为APP名和模型的小写名称的组合（用下划线组合）
    """
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_id = models.CharField(max_length=16, unique=True, primary_key=True)
    title = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre, related_name='movies', db_table='movie_genre')

    def __str__(self):
        return self.title

