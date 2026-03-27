from django.contrib import admin
from .models import WasteReport

@admin.register(WasteReport)
class WasteReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'waste_type', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority', 'waste_type')