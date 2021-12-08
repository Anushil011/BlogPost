from django.shortcuts import redirect, render
import os
from .models import Post
from .forms import PostForm
# Create your views here.

#index page view
def index(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html',{
        'posts':posts
    })

#specific post view
def post_details(request,post_slug):
    try:
        post= Post.objects.get(slug=post_slug) 
        return render(request,'posts/post.html',{
            'post_found': True,
            'postTitle':post.title,
            'postBody': post.body,
            'postSlug':post_slug
        })
    except Exception as exe:
        return render(request,'posts/post.html',{
            'post_found': False
    })

#adding a post view
def addPost(request):
    postForm = PostForm()
    if request.method == 'POST':
        postForm = PostForm(request.POST,request.FILES)
        if postForm.is_valid():
            postForm.save()
            return redirect('posts')
    
    return render(request,'posts/add-post-form.html',{'form':postForm})

#deleting a post view
def deletePost(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    if request.method == 'POST':
        post.delete()
        if len(post.image)>0:
            os.remove(post.image.path)
        return redirect('posts')
    return render(request, 'posts/delete-post.html', {'post': post})


#updating a post view
def updatePost(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    image = post.image
    postForm = PostForm(instance=post or None )
    if request.method == 'POST': 
        postForm = PostForm(request.POST,request.FILES,instance=post)
        if postForm.is_valid():
            postForm.save()
            if post.image != image:
                os.remove(image.path)
        return redirect('posts')
    return render(request, 'posts/add-post-form.html', {'form': postForm})
