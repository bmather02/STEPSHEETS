from django.contrib import admin
from .models import Choreographer, Sheet, Video
# Register your models here.
admin.site.register(Sheet)
admin.site.register(Choreographer)
admin.site.register(Video)