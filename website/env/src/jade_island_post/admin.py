from django.contrib import admin
from .models import JadeIslandPost

class JadeIslandPostAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',  'tags', 'body',)
    readonly_fields = ('date_updated', 'date_published',)
    ordering = ('-date_updated',)
    list_filter = ('is_approved',)
    filter_horizontal = ()
    fieldsets = ()
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('body', 'featured_image',),
    }),
    )

admin.site.register(JadeIslandPost, JadeIslandPostAdmin)