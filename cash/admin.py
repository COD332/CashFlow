from django.contrib import admin
from .models import Cost, Income, Category, Source

admin.site.register(Cost)
admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Source)