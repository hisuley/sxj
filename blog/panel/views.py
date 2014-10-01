from django.shortcuts import render
from panel.models import User
from panel.forms import UserForm
from django.shortcuts import render_to_response


def login(request):
    if not request.POST:
        return render(request, 'user/login.html')
    else:
        username = request.Post['username']
        password = request.Post['password']
        if User.checkPass(username=username, password=password) == 2:
            return render_to_response('blogpost/blog_display.html')


def logout(request):
    return render_to_response('user/logout_success.html')


def signin(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.clean_data['username']
            password = uf.clear_data['password']
            u = User.objects.create(username=username, password=password)
            u.save()
            return render_to_response('user/signin_success.html', {'username': username})
    else:
        uf = UserForm()
    return render_to_response('user/signin.html', {'uf': uf})