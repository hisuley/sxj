from django.shortcuts import render_to_response, get_object_or_404
from blogpost.models import BlogPost
from blogpost.forms import BlogForm
from django.http import HttpResponseRedirect


def blogList(request):
    blogs = BlogPost.objects.all()
    return render_to_response('blogpost/blog_list.html', {'blogs': blogs})


def blogEdit(request, id):
    blogs = get_object_or_404(BlogPost, id=id)
    if request.method == "POST":
        bf = BlogForm(request.POST, instance=blogs)
        if bf.is_valid():
            data = bf.cleaned_data
            title = data['title']
            body = data['body']
            if blogs:
                blogs.title = title
                blogs.body = body
                blogs.save()
            else:
                blogs = BlogPost(title=blogs.title, body=blogs.body)
                blogs.save()
            return HttpResponseRedirect('/blogpost/showdetail/%s/' % blogs.id)
    return render_to_response('blogpost/blog_edit.html', {'bf': BlogForm(instance=blogs)})


def blogWritenew(request):
    if request.method == "POST":
        bf = BlogForm(request.POST)
        if bf.is_valid():
            title = bf.cleaned_data['title']
            body = bf.cleaned_data['body']
            blogs = BlogPost.objects.create(title=title, body=body)
            blogs.save()
            id = BlogPost.objects.order_by('-timestamp')[0].id
            return HttpResponseRedirect('/blogpost/showdetail/%s/' % id)
    else:
        bf = BlogForm()
    return render_to_response('blogpost/blog_writenew.html', {'bf': bf})


def blogDelete(request, id):
    blog = BlogPost.objects.get(id=id)
    if blog:
        blog.delete()
        return HttpResponseRedirect('/blogpost/list')
    blogs = BlogPost.objects.all()
    return render_to_response('blogpost/blog_list.html', {'blogs': blogs})


def blogSearch(request):
    errors = []
    if 't' in request.POST and request.POST['t']:
        t = request.POST['t']
        if len(t) == 0:
            errors.append('Please enter a search term.')
        elif len(t) >= 20:
            errors.append('Please enter at most 20 characters.')
        else:
            blogs = BlogPost.objects.filter(title__icontains=t).order_by('-timestamp')
            return render_to_response('blogpost/blog_search_result.html', {'blogs': blogs})
    return render_to_response('blogpost/blog_search_result.html', {'errors': errors})


def blogShowDetail(request, id):
    blog = BlogPost.objects.get(id=id)
    if blog:
        return render_to_response('blogpost/blog_show_detail.html', {'blog': blog})
    else:
        blogs = BlogPost.objects.all()
        render_to_response('blogpost/blog_list.html', {'blogs': blogs})