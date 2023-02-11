from django.shortcuts import render
from .models import Image
from .forms import Formss
# Create your views here.
def index(request):
    if request.method=="POST":
        form = Formss(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = Formss()
    images=Image.objects.all()
    return render(request,'index.html',{'form':form,'img':images})