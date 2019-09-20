from django.contrib import admin
from .models import ChanBoard, ChanPost, ChanPostReply
# Register your models here.

admin.site.register(ChanBoard)
admin.site.register(ChanPost)
admin.site.register(ChanPostReply)