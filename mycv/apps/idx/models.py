from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
	category = models.CharField('Категория', max_length=200, db_index=True)
	idsort = models.PositiveSmallIntegerField('счетчик сортировки', default='1')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.category


class Block(models.Model):
	category = models.ForeignKey(Category, related_name='bloks', on_delete = models.CASCADE, verbose_name='Категория')
	name = models.CharField('Название блока', max_length=200, default="")
	slug = models.SlugField('тег для ид блока', max_length=200)
	idsort = models.PositiveSmallIntegerField('счетчик сортировки', default='1')
	startwork = models.PositiveSmallIntegerField('начальная дата', null=True, blank=True)
	endwork = models.PositiveSmallIntegerField('конечная дата', null=True, blank=True)
	# description = models.TextField('контент блока', blank=True)
	# content
	content  = HTMLField('Наполнение', null=True, blank=True, default="")

	class Meta:
		verbose_name = 'Блок'
		verbose_name_plural = 'Блоки'

	def __str__(self):
		return self.name
		

class Contacts(models.Model):
	name = models.CharField('Название блока', max_length=200, default="")
	slug = models.SlugField('тег для ид блока', max_length=200)
	idsort = models.PositiveSmallIntegerField('счетчик сортировки', default='1')
	content  = HTMLField('Наполнение', null=True, blank=True)

	class Meta:
		verbose_name = 'Контакты'
		verbose_name_plural = 'Контакты'

	def __str__(self):
		return self.name