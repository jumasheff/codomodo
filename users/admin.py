from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    exclude = ('first_name', 'last_name')
    list_display = ('email', 'username', 'name', 'is_superuser')


admin.site.register(User, UserAdmin)
