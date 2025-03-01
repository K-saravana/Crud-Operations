from django.shortcuts import render
from .models import Member

# Create your views here.
# this is for testing 
def index(request):

    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})
