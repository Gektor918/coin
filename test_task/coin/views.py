from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from coin.api_coin import *
from coin.models import *
from coin.serializers import *
from coin.api_coin import infocheck_and_create
from coin.newsapi import get_news
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout 



def index(request):
    return render(request,"coin/index.html")


def news(request):
    query = 'Bitcoin'
    return Response(get_news(query))


class RegisterView(TemplateView):
    def dispatch(self, request):
        if request.method == 'POST':
            if request.POST.get('password') == request.POST.get('password2'):
                User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
                user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
                login(request, user)
                return redirect("profile")
            else:
                return render(request,'coin/register.html')
        return render(request,'coin/register.html')


class LoginView(TemplateView):
    def dispatch(self, request):
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
            return redirect("profile")
        return render(request,"coin/login.html")


class ProfilePage(TemplateView):

    def dispatch(self, request):
        all_crypto = Crypto.objects.all()
        cod = [i.code for i in all_crypto]
        default = get_news('Bitcoin новости')

        try:
            need_profile = Profile.objects.get(user=request.user)
        except:
            need_profile = False
            if request.method == "POST":
                profile = Profile()
                profile.user = request.user
                profile.name = User.objects.get(username=request.user).get_username()
                crypto_ids = request.POST.getlist("id_crypto")
                profile.save()
                crypto = Crypto.objects.filter(id__in=crypto_ids)
                profile.crypto.set(crypto)
    
        try:
            news = get_news(request.POST['query'])
        except:
            news = default

        try:
            need_crypto = Crypto.objects.get(code=request.POST['code'])
            return render(request,"coin/profile.html",{'all_info':all_crypto,
                                                        'need_crypto':need_crypto,
                                                        'cod':cod,'news':news,
                                                        'need_profile': need_profile,
                                                        })
        except:
            return render(request,"coin/profile.html",{'all_info':all_crypto,
                                                        'cod':cod,'news':news,
                                                        'need_profile': need_profile,
                                                        })


def logout_user(request):
    logout(request)
    return redirect('Login')


class All_list_crypto_info(APIView):

    """ Getting a list of all cryptocurrencies, taking into account the exchange rate """

    def get(self,request):
        queryset_crypto = Crypto.objects.all()
        serializer_class = All_list_crypto_info_serializer(queryset_crypto, many=True)
        return Response({'info': serializer_class.data})


class All_list_crypto(APIView):

    """ Getting a list of all cryptocurrencies without taking into account the exchange rate """

    def get(self,request):
        queryset_crypto = Crypto.objects.all()
        serializer_class = All_list_crypto_serializer(queryset_crypto, many=True)
        return Response({'info': serializer_class.data})


class One_crypto(APIView):

    """ Obtaining information about a specific cryptocurrency by symbolic code """

    def post(self,request):
        try:
            need_crypto = Crypto.objects.get(code=request.data.get('code'))
            serializer_class = All_list_crypto_info_serializer(need_crypto)
            return Response({'info': serializer_class.data})
        except:
            return Response('No such character code exists')


class Add_crypto(APIView):

    """ Adding a new cryptocurrency """

    def post(self, request):
        new_cryto_seria = Add_crypto_serializer(data = request.data)
        new_cryto_seria.is_valid(raise_exception=True)
        new_cryto_seria.save()
        return Response(new_cryto_seria.data, status=201)


class CryptoUpdateView(generics.RetrieveUpdateAPIView):

    """ Cryptocurrency information update """

    serializer_class = Add_crypto_serializer
    queryset = Crypto.objects.all()

    def get_object(self):
        code = self.kwargs["code"]
        return Crypto.objects.get(code=code)


class CryptoDestroyView(generics.RetrieveDestroyAPIView):

    """ Deleting a Cryptocurrency """

    queryset = Crypto.objects.all()
    serializer_class = CryptoSerializer

    def get_object(self):
        code = self.kwargs["code"]
        return Crypto.objects.get(code=code)


class New_base(APIView):

    """ Obtaining data on cryptocurrencies, initial formation of a database """

    def post(self,request):
        infocheck_and_create()
        queryset_crypto = Crypto.objects.all()
        serializer_class = All_list_crypto_serializer(queryset_crypto, many=True)
        return Response({'info': serializer_class.data})


class Allfavorites(APIView):

    """ Selected cryptocurrencies """

    def get(self,request):
        queryset_Favorites = Favorites.objects.filter(user=request.user)
        serializer_class = FavoritesSerializer(queryset_Favorites, many=True)
        return Response({'info': serializer_class.data})


class Addfavorites(APIView):

    """ Add selected cryptocurrencies """

    def post(self, request):
        new_favorites_seria = FavoritesSerializer(data = request.data)
        new_favorites_seria.is_valid(raise_exception=True)
        new_favorites_seria.save(user=request.user)
        return Response(new_favorites_seria.data, status=201)


class NewsAPIView(APIView):

    """ NewsAPI """

    def get(self, request, format=None):
        query = 'Ethereum'
        return Response(get_news(query))
