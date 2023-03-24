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



class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя', null=True, blank=True, related_name='favorites')
    cryptos = models.ManyToManyField(Crypto, verbose_name='Избранные криптовалюты')

    def __str__(self):
        return 'Избранное юзера: {}'.format(self.user.username)
    
    class Meta:
        verbose_name = 'Избранные криптовалюты пользователя'
        verbose_name_plural = 'Избранные криптовалюты пользователей'

    