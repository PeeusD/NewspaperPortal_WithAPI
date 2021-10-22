from django.contrib import admin
from .models import Hindu, IndExp, EcoTimes, FinExp, BuisLine, BrillExp, HinTim, Toi, Mint
# Register your models here.

@admin.register(Hindu)
class Hinduadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']

@admin.register(IndExp)
class IndExpadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']

@admin.register(EcoTimes)
class EcoTimesadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']

@admin.register(FinExp)
class FinExpadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']


@admin.register(BuisLine)
class BuisLineadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']

@admin.register(BrillExp)
class BrillExpadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']

@admin.register(HinTim)
class HinTimadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']

@admin.register(Toi)
class Toiadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']


@admin.register(Mint)
class Mintadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dt', 'links']