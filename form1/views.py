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


@api_view(['GET'])
def infolistdetail(request,pk):
    info=personalinfo.objects.get(id=pk)
    serializer= personalinfoSerializer(info,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def infolistcreate(request):
    serializer= personalinfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def infolistupdate(request,pk):
    info=personalinfo.objects.get(id=pk)
    serializer= personalinfoSerializer(instance=info, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def infolistdelete(request,pk):
    info=personalinfo.objects.get(id=pk)
    info.delete()
    return Response('Its sucessfully deleted')