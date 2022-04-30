from django.shortcuts import render, redirect
from .models import BroadcastGroup, BroadcastMessage
from .forms import NewMessage

# Create your views here.

def home(request):
    return render(request, 'base.html')

def broadcastingMessage(request):
    group = BroadcastGroup.objects.all().values()
    broadcast = BroadcastMessage.objects.all().values()
    return render(request, 'broadcastPage.html', {'Groups':group, 'Broadcast':broadcast})

def broadcastingMessageForm(request):
    if request.method == 'POST':
        form = NewMessage(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print('form valid')
            if request.FILES.get('image') and request.FILES.get('video'):
                newObj = BroadcastMessage(title=request.POST['title'], description=request.POST['description'], image=request.FILES['image'], video=request.FILES['video'], ytvideo=request.POST['ytvideo'], broadcastgroup_id=1)
            elif request.FILES.get('image'):
                newObj = BroadcastMessage(title=request.POST['title'], description=request.POST['description'], image=request.FILES['image'], ytvideo=request.POST['ytvideo'], broadcastgroup_id=1)
            elif request.FILES.get('video'):
                newObj = BroadcastMessage(title=request.POST['title'], description=request.POST['description'], video=request.FILES['video'], ytvideo=request.POST['ytvideo'], broadcastgroup_id=1)
            else:
                newObj = BroadcastMessage(title=request.POST['title'], description=request.POST['description'], ytvideo=request.POST['ytvideo'], broadcastgroup_id=1)
            newObj.save()
            return redirect('broadcastingMessage')
    else:
        form = NewMessage()
    return render(request, 'addBroadcastForm.html',{'form':form})


