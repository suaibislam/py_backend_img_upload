from django.contrib import admin
from .models import Image
from .models import Student
# Register your models here.
admin.site.register(Student)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']