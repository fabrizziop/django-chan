from django.contrib import admin
from .models import ChanBoard, ChanPost, ChanPostReply
# Register your models here.

admin.site.register(ChanBoard)
#admin.site.register(ChanPost)
#admin.site.register(ChanPostReply)

class ChanPostAdmin(admin.ModelAdmin):
	list_display = ("id", "ip", "title", "date", "tripcode", "last_touch")
	search_fields = ("title", "content", "date", "tripcode", "ip", "last_touch")

class ChanPostReplyAdmin(admin.ModelAdmin):
	list_display = ("id", "ip", "container_ip", "title", "date", "tripcode")
	search_fields = ("title", "content", "date", "tripcode", "ip", "container_post__ip")

	def container_ip(self, obj):
		return obj.container_post.ip

admin.site.register(ChanPost, ChanPostAdmin)
admin.site.register(ChanPostReply, ChanPostReplyAdmin)