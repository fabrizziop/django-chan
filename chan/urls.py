from django.contrib import admin
from django.urls import include, path
from . import views
app_name = "chan"

urlpatterns = [
    path('boards/', views.all_boards, name='all_boards'),
    path('boards/<str:board_alias>/<int:page_number>/', views.specific_board, name='specific_board'),
    path('boards/<str:board_alias>/', views.specific_board_redirect, name='specific_board_redirect'),
	path('boards/<str:board_alias>/post/<int:post_id>/', views.specific_post, name='specific_post'),
	path('boards/<str:board_alias>/post/<int:post_id>/<str:post_successful>', views.specific_post, name='specific_post'),

]
