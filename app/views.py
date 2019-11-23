from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "login.html")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        group = None
        if user is not None:
            auth_login(request, user)
            group = CustomUser.objects.all().get(user_id__exact=request.user.id)
    return render(request, "result.html", {'group': group})