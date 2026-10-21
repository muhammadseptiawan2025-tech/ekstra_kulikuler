from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import siswa

class Siswa(admin.ModelAdmin):
    list_display = ('nama', 'kelas')
