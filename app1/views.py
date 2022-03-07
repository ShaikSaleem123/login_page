from django.shortcuts import render

# Create your views here.
def registerview(request):
    return render(request,'reg.html')

def index(request):
    return render(request,'index.html')