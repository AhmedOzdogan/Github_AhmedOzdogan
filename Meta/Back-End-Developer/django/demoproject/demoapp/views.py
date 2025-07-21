from django.http import HttpResponse, HttpResponsePermanentRedirect 
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def demo_home(request):
    if request.method == "POST":
        # Process form data here
        return HttpResponsePermanentRedirect(reverse('demoapp:login'))
    return render(request, 'demoapp/index.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        # Process form data here (authentication, etc.)
        return HttpResponsePermanentRedirect(reverse('demoapp:demo_home'))
    return render(request, 'demoapp/login.html')


def user_home(request, user_id):
    return HttpResponse("User ID: {}".format(user_id))

def user_profile(request, user_name, user_id):
    return HttpResponse("User Name: {}, User ID: {}".format(user_name, user_id))

@csrf_protect
def qryview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_id = request.POST.get('id')
        return render(request, 'demoapp/qryview.html', {'name': name, 'id': user_id})
    return render(request, 'demoapp/form.html')