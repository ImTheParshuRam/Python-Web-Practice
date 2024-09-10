from django.shortcuts import render
from django.http import HttpResponse #return home page

# def projects(request,pk):
#     return HttpResponse("This is my first application"+' '+str(pk))

# def HomePage(request):
#     return HttpResponse("This Is My first website")
# # Create your views here.

# def Welcome(request):
#     return HttpResponse("Hello, Welcome to my page")

def webpage1(request):
    message = "webdev project"
    number = 15
    context = {'msg': message, 'num': number}
    return render(request, 'page1.html')

def webpage2(request):
    return render(request, 'page2.html')