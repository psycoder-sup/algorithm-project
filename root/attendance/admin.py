from django.contrib import admin

from .models import DateModel

@admin.register(DateModel)
class DateAdmin(admin.ModelAdmin):
    list_display = ['today', 'attend_time', 'register', 'status']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('student')

