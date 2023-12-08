from django.contrib import admin
from .models import *

# Добавление моделей в админку
admin.site.register(Collection)
admin.site.register(Bookmark)
