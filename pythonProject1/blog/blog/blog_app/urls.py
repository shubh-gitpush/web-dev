from django.urls import path
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('about/',views.aboutview.as_view(),name ='about'),
    path('',views.postlistview.as_view(),name='post_list'),
    path('post/<int:pk>/',views.postdetailview.as_view(),name='post_detail'),
    path('post/new/',views.createpostview.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.postupdateview.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/',views.postdeleteview.as_view(),name='post_remove'),
    path('drafts/',views.draftlistview.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
    path('post/<int:pk>/image/',views.add_image,name='add_image'),
    path('post/navbar/',views.intro.as_view(),name='intro'),
    path('post/<int:pk>/reply/',views.reply_to_comment,name='reply_comment'),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
