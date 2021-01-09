from django.contrib import admin
from . import models


# Register your models here.
class bookingAdmin(admin.ModelAdmin):
    readonly_fields = ['books_ids', 'name_trip', 'price', ]

class slugify(admin.ModelAdmin):
    readonly_fields = ['slug']

class PostImageAdmin(admin.StackedInline):
    model = models.PostImage

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = models.Post

@admin.register(models.PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.carousel)
admin.site.register(models.booking)
admin.site.register(models.Post, slugify)
"""
    1. product
    2. gallery
    3. booking (generate id 4 alfabet)
    4. registrasi
    5. login
    
"""