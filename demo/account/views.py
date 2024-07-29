from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
# Create your views here.

def login(request):
    header = {'token': 'freya123'}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        res = {
            'name': username,
            'password': password,
            'status': 200,
            'message': 'OK'
        }
        #return HttpResponse(f"user{username}'s password is {password}")
        return JsonResponse(res)
    
    print(request.META.get('REMOTE_ADDR'))
    return render(request, 'login.html')

class RegisterView(View): # type: ignore
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        comfirm_password = request. POST.get('password2')
        return HttpResponse(f"username is {username}, and the password is {password}")