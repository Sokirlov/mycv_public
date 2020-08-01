from modeltranslation.translator import translator, register, TranslationOptions
from idx.models import Category, Block, Contacts

class ContactsTranslationOptions(TranslationOptions):
	fields = ('name', 'content')
	empty_values = {'name': '', 'content': ''}	
translator.register(Contacts, ContactsTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
	fields = ('category', 'idsort')
translator.register(Category, CategoryTranslationOptions)

class BlockTranslationOptions(TranslationOptions):
	fields = ('name', 'content')
	empty_values = {'name': '', 'content': ''}
translator.register(Block, BlockTranslationOptions)

