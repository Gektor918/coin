# Generated by Django 4.1.7 on 2023-03-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='code',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True, verbose_name='Символьный код'),
        ),
    ]