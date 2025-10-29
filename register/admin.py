from django.contrib import admin
from .models import allStudet

# Register your models here.



@admin.register(allStudet)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','stu_id','name','email', 'pw')



# admin.site.register(allStudet,StudentAdmin)
