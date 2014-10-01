from django.shortcuts import render_to_response, get_object_or_404
from blogpost.models import BlogPost
from blogpost.forms import BlogForm
from django.http import HttpResponseRedirect


def blogDisplay(request):
    blogs = BlogPost.objects.all()
    return render_to_response('blogpost/blog_display.html', {'blogs': blogs})


def blogEdit(request):
    blogs = get_object_or_404(BlogPost)
    if request.method == "POST":
        bf = BlogForm(request.POST, instance=blogs)
        if bf.is_valid():
            data = bf.clean_data
            title = data['title']
            body = data['body']
            if blogs:
                blogs.title = title
                blogs.body = body
                blogs.save()
            else:
                blogs = BlogPost(title=blogs.title, body=blogs.body)
                blogs.save()
            return HttpResponseRedirect('/blogpost/display/')
    return render_to_response('blogpost/blog_edit.html', {'bf': BlogForm(instance=blogs)})


def blogWritenew(request):
    if request.method == "POST":
        bf = BlogForm(request.POST)
        if bf.is_valid():
            title = bf.cleaned_data['title']
            body = bf.cleaned_data['body']
            #timestmap = request.POST['timestamp']
            blogs = BlogPost.objects.create(title=title, body=body)
            blogs.save()
            return HttpResponseRedirect('/blogpost/display/')
    else:
        bf = BlogForm()
    return render_to_response('blogpost/blog_writenew.html', {'bf': BlogForm()})


def blogDelete(request, id=''):
    blog = BlogPost.objects.get(id=id)
    if blog:
        blog.delete()
        blogs = BlogPost.objects.all()
        return render_to_response('blogpost/blog_display.html', {'blogs': blogs})


def blogSearch(request):
    error = False
    if 't' in request.POST and request.POST['t']:
        t = request.POST['t']
        if not t:
            error = True
        else:
            blogs = BlogPost.objects.filter(title__icontains=t).order_by('-timestamp')
            return render_to_response('blogpost/blog_search_result.html', {'blogs': blogs})
    return render_to_response('blogpost/blog_display.html',{'errors': error})