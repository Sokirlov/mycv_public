# Generated by Django 3.0.6 on 2020-06-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='block',
            name='description',
            field=models.TextField(blank=True, verbose_name='контент блока'),
        ),
        migrations.AlterField(
            model_name='block',
            name='name',
            field=models.CharField(max_length=200, verbose_name='название блока'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(db_index=True, max_length=200, verbose_name='категория'),
        ),
    ]
