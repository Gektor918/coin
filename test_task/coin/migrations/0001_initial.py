# Generated by Django 4.1.7 on 2023-03-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=60, null=True, verbose_name='Символьный код')),
                ('name', models.CharField(blank=True, max_length=60, null=True, verbose_name='Имя')),
                ('current_rate', models.CharField(blank=True, max_length=60, null=True, verbose_name='Текущий курс в USD')),
                ('exchange_rate', models.JSONField(blank=True, null=True, verbose_name='Обменный курс')),
            ],
        ),
    ]