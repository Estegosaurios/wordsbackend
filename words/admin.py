from django.contrib import admin
from words.models import Tag, Word

@admin.register(Tag, Word)
class PersonAdmin(admin.ModelAdmin):
    pass
