from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


from .models import Category, Block, Contacts


class CategoryAdmin(TranslationAdmin):
    list_display = ['category', 'idsort']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'idsort', 'category', 'slug', 'startwork', 'endwork']
    list_filter = ('category','slug')
    fieldsets =(
        ('Заголовок', {'fields':('category', 'name', ('slug', 'idsort'), ('startwork', 'endwork'),'content',),}),
        )
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
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