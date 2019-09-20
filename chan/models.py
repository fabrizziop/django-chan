from django.db import models
from django.utils import timezone

class ChanBoard(models.Model):
	board_name = models.CharField(max_length=300)
	board_alias = models.CharField(max_length=32)
	def __str__(self):
		return self.board_name

class ChanPost(models.Model):
	title = models.CharField(max_length = 280, default="", blank=True)
	content = models.TextField(default="", blank=True)
	date = models.DateTimeField(default=timezone.now)
	tripcode = models.CharField(max_length=128, default="", blank=True)
	image = models.ImageField(blank=True, upload_to='chan_images/')
	ip = models.CharField(max_length=128, default="", blank=True)
	last_touch = models.DateTimeField(default=timezone.now)
	container_board = models.ForeignKey(ChanBoard, on_delete=models.CASCADE)


	def __str__(self):
		return self.container_board.board_alias + "#"+str(self.id)+ " " + self.title

class ChanPostReply(models.Model):
	title = models.CharField(max_length = 280, default="", blank=True)
	content = models.TextField(default="", blank=True)
	date = models.DateTimeField(default=timezone.now)
	tripcode = models.CharField(max_length=128, default="", blank=True)
	image = models.ImageField(blank=True, upload_to='chan_images/')
	ip = models.CharField(max_length=128, default="", blank=True)
	container_post = models.ForeignKey(ChanPost, on_delete=models.CASCADE)

	def __str__(self):
		return self.container_post.container_board.board_alias + "#"+str(self.container_post.id)+ " r# " + str(self.id)
