from django.shortcuts import render, get_object_or_404
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ChanBoard, ChanPost, ChanPostReply
from .forms import ChanPostForm, ChanPostReplyForm
from .secrets import *
import hashlib
import requests
# Create your views here.


def all_boards(request):
	chan_boards = ChanBoard.objects.all()
	context = {
	"boards": chan_boards
	}
	return render(request, 'chan/index.html', context)

def specific_board_redirect(request, board_alias):
	current_board = get_object_or_404(ChanBoard, board_alias=board_alias)
	return HttpResponseRedirect(reverse('chan:specific_board', args=(board_alias, 1)))

def specific_board(request, board_alias, page_number):
	current_board = get_object_or_404(ChanBoard, board_alias=board_alias)
	form = ChanPostForm(request.POST, request.FILES or None, None)
	captcha_ok = True
	if request.method == "POST":
		if form.is_valid():
			captcha_ok = False
			recaptcha_response = request.POST.get("g-recaptcha-response")
			recaptcha_validation_request = requests.post("https://www.google.com/recaptcha/api/siteverify",
				data={
				'secret': recaptcha_secret_key,
				'response': recaptcha_response
				})
			recaptcha_validation_result = recaptcha_validation_request.json()
			if recaptcha_validation_result['success']:
				captcha_ok = True
				print("CAPTCHA OK")
				obj = form.save(commit=False)
				obj.ip = request.META.get('HTTP_X_REAL_IP') or "0.0.0.0 PLACEHOLDER"
				if obj.tripcode != "":
					obj.tripcode = hashlib.sha3_224(bytes(obj.tripcode, "utf-8")).hexdigest()
				obj.container_board = ChanBoard.objects.get(board_alias=board_alias)
				if obj.content != "":
					obj.save()
					print("VALID")
					return HttpResponseRedirect(reverse('chan:specific_post', args=(board_alias, obj.id, "success")))
			else:
				print("CAPTCHA FAIL")
	paginator = Paginator(current_board.chanpost_set.order_by("-last_touch").all(), 5)
	try:
		current_posts = paginator.page(page_number)
	except EmptyPage:
		current_posts = paginator.page(paginator.num_pages)
	replies = []
	for post in current_posts:
		replies.append(list(post.chanpostreply_set.order_by("-date")[:5])[::-1])
	zipped = list(zip(current_posts, replies))
	#print(zipped[0])
	#print(zipped[1])
	context = {
		"board": current_board,
		"recaptcha_site_key": recaptcha_site_key,
		"captcha_ok": captcha_ok,
		"form": form,
		"paginator": current_posts,
		"replies": replies,
		"zipped": zipped
	}
	return render(request, 'chan/board.html', context)


def specific_post(request, board_alias, post_id, post_successful=None):
	current_board = get_object_or_404(ChanBoard, board_alias=board_alias)
	current_post = get_object_or_404(current_board.chanpost_set, id=post_id)
	form = ChanPostReplyForm(request.POST, request.FILES or None, None)
	captcha_ok = True
	if request.method == "POST":
		if form.is_valid():
			captcha_ok = False
			recaptcha_response = request.POST.get("g-recaptcha-response")
			recaptcha_validation_request = requests.post("https://www.google.com/recaptcha/api/siteverify",
				data={
				'secret': recaptcha_secret_key,
				'response': recaptcha_response
				})
			recaptcha_validation_result = recaptcha_validation_request.json()
			if recaptcha_validation_result['success']:
				captcha_ok = True
				print("CAPTCHA OK")
				obj = form.save(commit=False)
				obj.ip = request.META.get('HTTP_X_REAL_IP') or "0.0.0.0 PLACEHOLDER"
				if obj.tripcode != "":
					obj.tripcode = hashlib.sha3_224(bytes(obj.tripcode, "utf-8")).hexdigest()
				obj.container_post = ChanPost.objects.get(id=post_id)
				if obj.content != "":
					obj.container_post.last_touch = timezone.now()
					obj.container_post.save()
					obj.save()
					print("VALID")
				form = ChanPostReplyForm()
			else:
				print("CAPTCHA FAIL")
	replies = current_post.chanpostreply_set.all()
	if post_successful == "success":
		post_successful = True
	context = {
	"board": current_board,
	"recaptcha_site_key": recaptcha_site_key,
	"captcha_ok": captcha_ok,
	"post": current_post,
	"form": form,
	"replies": replies,
	"post_successful": post_successful
	}
	return render(request, 'chan/post.html', context)

def make_post_in_board(request, board_alias):
	chan_boards = ChanBoard.objects.all()
	context = {
	"boards": chan_boards
	}
	return render(request, 'chan/index.html', context)

