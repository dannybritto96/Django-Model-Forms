from django.shortcuts import render
from django.http import HttpResponse
from .forms import DetailsForm

# Create your views here.
def index(request):
    form = DetailsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Fail")

    return render(request,"index.html",{'form':form})
