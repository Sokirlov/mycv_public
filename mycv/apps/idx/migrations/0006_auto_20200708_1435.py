# Generated by Django 3.0.6 on 2020-07-08 11:35

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('idx', '0005_auto_20200707_2253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': 'Блок', 'verbose_name_plural': 'Блоки'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='block',
            name='idsort',
            field=models.PositiveSmallIntegerField(default='1', verbose_name='счетчик сортировки'),
        ),
        migrations.AlterField(
            model_name='block',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloks', to='idx.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='block',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Наполнение'),
        ),
        migrations.AlterField(
            model_name='block',
            name='endwork',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='конечная дата'),
        ),
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название блока'),
        ),
        migrations.AlterField(
            model_name='block',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='тег для ид блока'),
        ),
        migrations.AlterField(
            model_name='block',
            name='startwork',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='начальная дата'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Категория'),
        ),
    ]
