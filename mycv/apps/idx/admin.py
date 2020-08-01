from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import Category, Block, Contacts


class CategoryAdmin(TranslationAdmin):
    list_display = ['category', 'idsort']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'idsort', 'category', 'slug', 'startwork', 'endwork']
    list_filter = ('category','slug')
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(Block, ProductAdmin)

# @admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    list_display = ['name', 'idsort']
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(Contacts, ContactsAdmin)