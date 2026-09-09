from django.contrib import admin

from .models import HeroStat, NewsItem, Tenant, TenantCategory


@admin.register(HeroStat)
class HeroStatAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "order")
    ordering = ("order",)


@admin.register(TenantCategory)
class TenantCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_featured")
    list_filter = ("category", "is_featured")
    search_fields = ("name", "description")


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    ordering = ("-published_date",)
