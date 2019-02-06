from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the Dashboard.")

def index(request):
    return render(request, 'dashboard/index.html', {})

#def post_list(request):
#    return render(request, 'dashboard/index.html', {})
