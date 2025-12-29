from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ("Welcome to the task management system")
def contact(request):
    return HttpResponse("<h1 style='color: red '> This is Contact page</h1>")
def show_task (request) :
    return HttpResponse ( " This is Show Tasks")
def show_specific_tusk(request , id):
    print("id" , id)
    print("id type" , type(id) )
    return HttpResponse ( f" This is Specific Task page {id} ")