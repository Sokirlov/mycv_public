# Generated by Django 3.0.7 on 2020-07-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idx', '0017_auto_20200713_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_en',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_ru',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_uk',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='idsort_en',
            field=models.PositiveSmallIntegerField(default='1', null=True, verbose_name='счетчик сортировки'),
        ),
        migrations.AddField(
            model_name='category',
            name='idsort_ru',
            field=models.PositiveSmallIntegerField(default='1', null=True, verbose_name='счетчик сортировки'),
        ),
        migrations.AddField(
            model_name='category',
            name='idsort_uk',
            field=models.PositiveSmallIntegerField(default='1', null=True, verbose_name='счетчик сортировки'),
        ),
    ]