from django.contrib import admin
from coin.models import Crypto, Favorites

admin.site.register(Crypto)
admin.site.register(Favorites)