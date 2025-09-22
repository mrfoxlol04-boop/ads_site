# ads/admin.py

from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date']
    list_filter = ['publication_date']
    search_fields = ['title', 'short_description']
    date_hierarchy = 'publication_date'