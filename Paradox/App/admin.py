from django.contrib import admin
from .models import Product
from .models import Rubric
# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('title','text','price','date',)
    list_display_links = ('title',)
    search_fields = ('title','text',)
admin.site.register(Product, Admin)
admin.site.register(Rubric)