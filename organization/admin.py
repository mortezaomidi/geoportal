from django.contrib import admin

from .models import Organization, Metadata

admin.site.register(Organization)
admin.site.register(Metadata)
