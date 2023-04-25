from django.db import models
from django.contrib.auth.models import User


class Crypto(models.Model):
    code = models.CharField(max_length=60, null=False, blank=False, unique=True, verbose_name='Символьный код')
    name = models.CharField(max_length=60, null=False, blank=False, verbose_name='Имя')
    current_rate = models.CharField(max_length=60, null=False, blank=False, verbose_name='Текущий курс в USD')
    exchange_rate = models.JSONField(encoder=None, decoder=None, null=True, blank=True, verbose_name='Обменный курс')
    
    def __str__(self):
        return 'Имя: {}'.format(self.name)
    
    class Meta:
        verbose_name = 'Криптовалюту'
        verbose_name_plural = 'Криптовалюта'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    crypto = models.ManyToManyField(Crypto, through="Favorites")

    def __str__(self):
        return 'Избранное юзера: {}'.format(self.name)


class Favorites(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Имя пользователя', related_name='favorites')
    cryptos = models.ForeignKey(Crypto, on_delete=models.CASCADE, verbose_name='Избранные криптовалюты')

    def __str__(self):
        return 'Избранное юзера: {}'.format(self.user)
    
    class Meta:
        verbose_name = 'Избранные криптовалюты пользователя'
        verbose_name_plural = 'Избранные криптовалюты пользователей'
