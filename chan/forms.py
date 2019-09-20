from django import forms
from .models import (ChanBoard, ChanPost, ChanPostReply)
from django.core.exceptions import ValidationError

def file_validator(file):
	max_size = 2048576
	if file.size > max_size:
		raise ValidationError

class ChanPostForm(forms.ModelForm):
	image = forms.ImageField(validators=[file_validator], required=False)
	class Meta:
		model = ChanPost
		fields = ['title', 'content', 'tripcode', 'image']

class ChanPostReplyForm(forms.ModelForm):
	image = forms.ImageField(validators=[file_validator], required=False)
	class Meta:
		model = ChanPostReply
		fields = ['title', 'content', 'tripcode', 'image']