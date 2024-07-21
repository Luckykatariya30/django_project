from django.shortcuts import render, HttpResponse
from .models import Image 
from .forms import ImageForm

# Create your views here.


def home(request,pk =0):
    if request.method == "POST":
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    context = {
        'form':form,
        'img': img
    }
    if pk:
        try:
            img_to_be_remoce = Image.objects.get(id=pk)
            img_to_be_remoce.delete()
        except:
            return render(request , 'home.html', context)
    return render(request , 'home.html',context)


def remove_img(request, pk=0):
    if pk:
        try:
            emp_to_be_remoce = Image.objects.get(id=pk)
            emp_to_be_remoce.delete()
        except:
            return HttpResponse("this employee details are worng ....")
    emps = Image.objects.all()
    context = {
        'emps': emps
    }

    return render(request, "home.html", context)