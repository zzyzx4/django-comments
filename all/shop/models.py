from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField("Категория", max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField("Брэнд", max_length=100)

    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, "Категория")
    brand = models.ForeignKey(Brand, "Брэнд")
    title = models.CharField("Товар", max_length=100)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена")
    #image = models.ImageField(upload_to='product', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField(verbose_name="Модерация", default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return "{}".format(self.user)
