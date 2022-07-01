from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import Account


# Register your models here.


class AccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'picture')}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email, is_staff, is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'picture')}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
