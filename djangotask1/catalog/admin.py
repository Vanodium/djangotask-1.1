from django.contrib import admin
from .models import Tag, Category, Item

admin.site.register(Tag)
admin.site.register(Category)
# admin.site.register(Item)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'image_tmb'
    )
    list_editable = ('is_published',)
    list_editable_links = ('name',)
    filter_horizontal = ('tags',)
