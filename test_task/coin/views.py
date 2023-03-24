from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from coin.api_coin import *
from coin.models import *
from coin.serializers import *
from rest_framework.permissions import IsAuthenticated
from coin.api_coin import infocheck_and_create
from coin.newsapi import get_news



class All_list_crypto_info(APIView):
    """ Получение списка всех криптовалют c учетом обменного курса """
    permission_classes = [IsAuthenticated]

    def get(self,request):
        queryset_crypto = Crypto.objects.all()
        serializer_class = All_list_crypto_info_serializer(queryset_crypto, many=True)
        return Response({'info': serializer_class.data})


class All_list_crypto(APIView):
    """ Получение списка всех криптовалют без учета обменного курса """
    permission_classes = [IsAuthenticated]

    def get(self,request):
        queryset_crypto = Crypto.objects.all()
        serializer_class = All_list_crypto_serializer(queryset_crypto, many=True)
        return Response({'info': serializer_class.data})


class One_crypto(APIView):
    """ Получение информации о конкретной криптовалюте по символьному коду """
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            need_crypto = Crypto.objects.get(code=request.data.get('code'))
            serializer_class = All_list_crypto_info_serializer(need_crypto)
            return Response({'info': serializer_class.data})
        except:
            return Response('Такого символьного кода не существует')


class Add_crypto(APIView):
    """ Добавление новой криптовалюты """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        new_cryto_seria = Add_crypto_serializer(data = request.data)
        new_cryto_seria.is_valid(raise_exception=True)
        new_cryto_seria.save()
        return Response(new_cryto_seria.data, status=201)


class CryptoUpdateView(generics.RetrieveUpdateAPIView):
    """ Обновление информации о криптовалюте """
    permission_classes = [IsAuthenticated]

    serializer_class = Add_crypto_serializer
    queryset = Crypto.objects.all()

    def get_object(self):
        code = self.kwargs["code"]
        return Crypto.objects.get(code=code)


class CryptoDestroyView(generics.RetrieveDestroyAPIView):
    """ Удаление криптовалюты """
    permission_classes = [IsAuthenticated]

    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer

    def get_object(self):
        code = self.kwargs["code"]
        return Crypto.objects.get(code=code)


class New_base(APIView):
    """ Получения данных о курсах криптовалют """
    permission_classes = [IsAuthenticated]

    def post(self,request):
        infocheck_and_create()
        queryset_crypto = Crypto.objects.all()
        serializer_class = All_list_crypto_serializer(queryset_crypto, many=True)
        return Response({'info': serializer_class.data})


class Allfavorites(APIView):

    def get(self,request):
        queryset_Favorites = Favorites.objects.filter(user=request.user)
        serializer_class = FavoritesSerializer(queryset_Favorites, many=True)
        return Response({'info': serializer_class.data})


class Addfavorites(APIView):

    def post(self, request):
        new_favorites_seria = FavoritesSerializer(data = request.data)
        new_favorites_seria.is_valid(raise_exception=True)
        new_favorites_seria.save(user=request.user)
        return Response(new_favorites_seria.data, status=201)


class NewsAPIView(APIView):
    def get(self, request, format=None):
        query = 'Ethereum'
        return Response(get_news(query))


