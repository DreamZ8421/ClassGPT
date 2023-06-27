from django.contrib import admin
from Home.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass