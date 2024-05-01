from django.contrib import admin
from .models import Cost, Income, Category, Source

class CostAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date', 'category']
    list_filter = ['date', 'category']
    search_fields = ['title', 'description']
    readonly_fields = ['date']

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date', 'source']
    list_filter = ['date', 'source']
    search_fields = ['title', 'description']
    readonly_fields = ['date']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

admin.site.register(Cost, CostAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)