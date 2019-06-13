from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.\
from .form import AddForm

def index(request):
    return render(request, 'extend/index.html')


def csrf1(request):
    return render(request, 'extend/login.html')


def csrf2(request):
    return HttpResponse("登陆成功")


def login(request):
    if request.method == 'GET':
        form = AddForm()
        return render(request, 'extend/login.html', {'form': form})
    elif request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            return HttpResponse(username+str(age))
