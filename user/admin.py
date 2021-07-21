from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
UserAdmin.fieldsets += ('Custom Fields', {'fields': ['name', 'bio', 'experience', 'skills', 'contact_num', 'employee']}),
admin.site.register(User, UserAdmin)
