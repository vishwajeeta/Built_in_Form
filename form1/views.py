from django.shortcuts import render,redirect
from .models import personalinfo
from .form import personalinfoForm

# Django rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
# importing serializer we created earlier
from .serializer import personalinfoSerializer

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

@api_view(['GET'])
def infolist(request):
    info=personalinfo.objects.all()
    serializer= personalinfoSerializer(info,many=True)
    return Response(serializer.data)