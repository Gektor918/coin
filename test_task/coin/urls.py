from django.urls import path
from coin.views import *

urlpatterns = [
    path('all/info', All_list_crypto_info.as_view()),
    path('all/crypto', All_list_crypto.as_view()),
    path('one/crypto', One_crypto.as_view()),
    path('add/crypto', Add_crypto.as_view()),
    path('update/crypto/<str:code>/', CryptoUpdateView.as_view()),
    path('destroy/crypto/<str:code>/', CryptoDestroyView.as_view()),
    path('new_base', New_base.as_view()),
    path('add/favorite', Addfavorites.as_view()),
    path('all/favorite', Allfavorites.as_view()),
    path('news', NewsAPIView.as_view()),
]