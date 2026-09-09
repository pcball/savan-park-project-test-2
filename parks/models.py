from django.db import models
from django.utils.translation import gettext_lazy as _


class HeroStat(models.Model):
    label = models.CharField(_("label"), max_length=60)
    value = models.CharField(_("value"), max_length=20)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} {self.label}"


class TenantCategory(models.Model):
    name = models.CharField(_("name"), max_length=80)
    slug = models.SlugField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = "Tenant categories"

    def __str__(self):
        return self.name


class Tenant(models.Model):
    name = models.CharField(_("company name"), max_length=120)
    category = models.ForeignKey(
        TenantCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="tenants"
    )
    description = models.CharField(_("description"), max_length=200, blank=True)
    logo_letter = models.CharField(max_length=2, blank=True)
    logo_color = models.CharField(max_length=20, default="#4c1d95")
    website = models.URLField(blank=True)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.logo_letter and self.name:
            self.logo_letter = self.name[0].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(_("title"), max_length=200)
    summary = models.TextField(_("summary"), blank=True)
    published_date = models.DateField(_("published date"))

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
