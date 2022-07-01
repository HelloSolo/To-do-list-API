from django.contrib import admin
from .models import UserList

# Register your models here.


@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'remainderDate',
        'remainderTime',
        'remainder'
    ]

    autocomplete_fields = ['user_id']
