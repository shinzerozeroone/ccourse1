from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Premium(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class PremAlbum(models.Model):
    post = models.ForeignKey(Premium, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Vip(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class VipAlbum(models.Model):
    post = models.ForeignKey(Vip, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Full(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class FullAlbum(models.Model):
    post = models.ForeignKey(Full, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


#----------- Other tables -----------#


class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField("Изображение", upload_to='../media/images')
    max_length = models.IntegerField("Максимальный размер", null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категерия'
        verbose_name_plural = 'Категории'


class Contact(models.Model):
    """Форма обратной связи"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


# Reviews


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey(Author, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
