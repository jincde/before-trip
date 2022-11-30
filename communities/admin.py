from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Article

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Article, PostAdmin)