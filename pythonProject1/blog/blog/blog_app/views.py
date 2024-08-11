from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog_app.models import Post,comment,Reply
from blog_app.forms import postform,commentform,ReplyForm
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import DeleteView
# Create your views here.

class aboutview(TemplateView):
    template_name= 'blog_app/about.html'
class intro(TemplateView):
    template_name='blog_app/intro.html'

class postlistview(ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#grab post model object then filter out published date less than equal to current time than order them in published date - is for ascending order
class postdetailview(DetailView):
    model=Post
    template_name = 'blog_app/post_detail.html'
class createpostview(LoginRequiredMixin,CreateView):
    login_url='/login/' # URL to redirect to if the user is not authenticated
    redirect_field_name='blog_app/post_detail.html'
    form_class=postform
    model=Post

#@login_required decorator is only valid for function not class

class postupdateview(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog_app/post_detail.html'
    form_class=postform
    model=Post


class postdeleteview(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')
    template_name = 'blog_app/post_confirm_delete.html'
class draftlistview(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog_app/post_list.html'
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

@login_required
def reply_to_comment(request, pk):
    Comment = get_object_or_404(comment, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            # Step 3: If the form is valid, save the reply
            reply.Comment = Comment
            # Step 4: Associate the reply with the comment
            reply.author = request.user
            reply.save()
            return redirect('post_detail', pk=Comment.post.pk)
    else:
        form = ReplyForm()
    return render(request, 'blog_app/reply_comment.html', {'form': form})

def post_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        mentions = parse_mentions(content)
        # Save mentions
        for mention in mentions:
            Mention.objects.create(user=mention, content=content)
        # Save the original content or do other processing
    return render(request, 'blog_app/post_comment.html')
@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the blog post list page
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def display_video(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'display_video.html', {'video': video})
@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=commentform()
    return render(request,'blog_app/comment_form.html',{'form':form})
@login_required
def add_image(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form=postform(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=pk)
    else:
        form = postform(instance=post)  # Pass instance=post to edit the existing post
    return render(request, 'blog_app/add_image.html', {'form': form},{'post' : post})

@login_required
def comment_approve(request,pk):
    Comment=get_object_or_404(comment,pk=pk)
    Comment.approve()
    return redirect('post_detail',pk=Comment.post.pk)
@login_required
def comment_remove(request,pk):
    Comment=get_object_or_404(comment,pk=pk)
    Post_pk=Comment.post.pk #   # Retrieve the primary key of the post associated with the comment
    Comment.delete()
    return redirect('post_detail',pk=Post_pk)
