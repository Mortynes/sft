from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    image = models.ImageField(verbose_name='Изображение услуги')

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название преимущества")
    description = models.TextField(verbose_name="Описание преимущества")

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    image = models.ImageField(verbose_name='Изображение проекта')

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    position = models.CharField(max_length=255, verbose_name='Должность')
    bio = models.TextField(verbose_name='Биография')
    image = models.ImageField(verbose_name='Фотография')

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Команда"

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название сертификата')
    description = models.TextField(verbose_name='Описание сертификата')
    image = models.ImageField(verbose_name='Изображение сертификата')
    issued_at = models.DateField(verbose_name='Дата выдачи')
    expired_at = models.DateField(verbose_name='Дата истечения срока действия')

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.title
