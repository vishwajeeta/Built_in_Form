from django.shortcuts import render,redirect
from .models import personalinfo
from .form import personalinfoForm
# Create your views here.
def home(request):
    data=personalinfo.objects.all()
    if request.method == 'POST':
        form=personalinfoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
    form=personalinfoForm()
    return render(request,'index.html',{'data':data,'form':form})