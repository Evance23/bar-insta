from django.shortcuts import render
from django.http  import HttpResponse
from . import Views 

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Insta')



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(render, insta/index.html)
