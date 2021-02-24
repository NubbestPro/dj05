from django.shortcuts import render

# Create your views here.
def home(request):
    info="This is something new. "
    return render(request,"index.html",{"info": info})