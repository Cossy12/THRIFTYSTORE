from django.contrib import admin
from .models import UserProfile

# Register your models here.

  
from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(UserProfile)



class UserAdmin(admin.ModelAdmin):
    list_display=('username','is_customer','is_manager','phone','city','postalcode')
admin.site.register(User,UserAdmin)
