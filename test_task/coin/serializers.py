from rest_framework import serializers
from coin.models import *


class All_list_crypto_info_serializer(serializers.ModelSerializer):
    exchange_rate = serializers.JSONField()
    class Meta:
        model = Crypto
        fields = ['id', 'code', 'name', 'current_rate', 'exchange_rate']


class All_list_crypto_serializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        exclude = ['exchange_rate']


class One_crypto_serializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['code']


class Add_crypto_serializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['id', 'code', 'name', 'current_rate']

    def create(self, validated_data):
        return Crypto.objects.create(**validated_data)


class Add_crypto_serializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['id', 'code', 'name', 'current_rate']

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.current_rate = validated_data.get('current_rate', instance.current_rate)
        instance.save()
        return instance


class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['id', 'code', 'name', 'current_rate']

    def destroy(self, instance):
        instance.delete()


class FavoritesSerializer(serializers.ModelSerializer):
    #cryptos = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Favorites
        fields = ['user', 'cryptos']