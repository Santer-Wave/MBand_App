from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    birthday = models.DateField()
    district = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    statusChoices = (
        ('Нет статуса', 'Нет статуса'),
        ('В поисках группы', 'В поисках группы'),
        ('В поисках людей в группу', 'В поисках людей в группу')
    )
    status = models.CharField(max_length=64, blank=True, choices=statusChoices, default=statusChoices[0])
    linkYT = models.CharField(max_length=256, blank=True)
    linkVK = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.user} {self.first_name} {self.last_name} {self.status}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Avatar(models.Model):
    user = models.OneToOneField(User, related_name='avatars', on_delete=models.CASCADE)
    photo = models.ImageField(_("Image"), upload_to=upload_to, blank=True)


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.subscribed}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    skillChoices = (
        ("Гитара", "Гитара"),
        ("Скрипка", "Скрипка"),
        ("Вокал", "Вокал"),
        ("Синтезатор", "Синтезатор"),
        ("Барабаны", "Барабаны")
    )
    skill = models.CharField(max_length=64, choices=skillChoices, blank=True)

    def __str__(self):
        return f"{self.user} {self.skill}"

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Genre(models.Model):
    user = models.ForeignKey(User, related_name='genres', on_delete=models.CASCADE)
    genreChoices = (
        ('Фолк', 'Фолк'),
        ('Рок', 'Рок'),
        ('Рэп', 'Рэп'),
        ('Металл', 'Металл'),
        ('Классика', 'Классика')
    )
    genre = models.CharField(max_length=64, choices=genreChoices, blank=True)

    def __str__(self):
        return f"{self.user} {self.genre}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
