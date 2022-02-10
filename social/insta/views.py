from django.shortcuts import render
from django.http  import HttpResponse 
from django.contrib.auth.decorators import login_required


# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Insta')



def index(request):
    return render(request, "index.html") 


# @login_required(login_url='/accounts/login/')
#         def article(request, article_id):