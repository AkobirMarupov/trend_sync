from django.contrib import admin

from .models import User


@admin.register(User)
class CusomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')


    fieldsets = (
    ('User', {'fields': ('username', 'password', 'email')}),
    ('Personal info', {'fields': ('first_name', 'last_name', 'avatar', 'language')}),
    ('Permissions', {'fields': ('is_active', 'is_superuser')}),
)
    


