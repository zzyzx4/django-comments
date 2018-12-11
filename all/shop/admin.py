from django.contrib import admin
from .models import Category, Brand, Product, Commentary

from django_summernote.admin import SummernoteModelAdmin


class ShopModel(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'description', 'text'


class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created', 'moderation')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ShopModel)
admin.site.register(Commentary, CommentaryAdmin)

