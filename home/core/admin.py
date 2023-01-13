from django.contrib import admin
from .models import Post,Type,SubType

admin.site.register(Post)
admin.site.register(Type)
admin.site.register(SubType)