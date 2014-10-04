from django.shortcuts import render
from panel.models import User
from panel.forms import UserForm
from django.shortcuts import render_to_response
from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            u = User.objects.get(username=username)
            if u.password == password:
                return render_to_response('blogpost/blog_list.html')
            else:
                return HttpResponse('Please signin or check your username and password')
    return render_to_response('user/login.html')


def logout(request):
    return render_to_response('user/logout_success.html')


def signin(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            u = User.objects.create(username=username, password=password)
            u.save()
            return render_to_response('user/signin_success.html', {'username': username})
    else:
        uf = UserForm()
    return render_to_response('user/signin.html', {'uf': uf})