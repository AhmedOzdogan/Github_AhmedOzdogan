from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin): 
    list_display = ("name", "price", "category", "available") 
    search_fields = ("name__icontains", "category__icontains")


from django.contrib.auth.models import User 
# Unregister the provided model admin: 
 
admin.site.unregister(User) 

from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True # type: ignore 
            form.base_fields['email'].disabled = True # type: ignore
            form.base_fields['is_staff'].disabled = True # type: ignore
            form.base_fields['is_active'].disabled = True # type: ignore
            form.base_fields['is_superuser'].disabled = True # type: ignore
            

        return form 