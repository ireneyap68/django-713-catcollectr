from django.contrib import admin
from .models import Cat, CatToy, videos


# Register your models here.
admin.site.register(Cat)
admin.site.register(CatToy)
admin.site.register(videos)
