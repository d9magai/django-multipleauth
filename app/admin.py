from django.contrib import admin
from django.contrib.auth.hashers import make_password

from app.models import Owner, User


class OwnerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            user = Owner.objects.get(pk=obj.pk)
            if not user.password == obj.password:
                obj.password = make_password(obj.password)
        else:
            obj.password = make_password(obj.password)
        obj.save()
    list_display = ['name', 'email']
    ordering = ['name']


admin.site.register(Owner, OwnerAdmin)


class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            user = User.objects.get(pk=obj.pk)
            if not user.password == obj.password:
                obj.password = make_password(obj.password)
        else:
            obj.password = make_password(obj.password)
        obj.save()
    list_display = ['name', 'email']
    ordering = ['name']


admin.site.register(User, UserAdmin)
