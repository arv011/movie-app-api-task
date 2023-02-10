from django.contrib import admin
from accounts.models import User,RequestCounter
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

class RequestCounterAdmin(admin.ModelAdmin):
    list_display = ('counts','is_deleted','updated','created')

admin.site.register(User, UserAdmin)
admin.site.register(RequestCounter, RequestCounterAdmin)
