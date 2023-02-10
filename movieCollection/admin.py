from django.contrib import admin
from movieCollection.models import UserMovieCollection
# Register your models here.

class UserMovieCollectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('uuid',)
admin.site.register(UserMovieCollection, UserMovieCollectionAdmin)
