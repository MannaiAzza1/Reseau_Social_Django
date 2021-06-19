from django.shortcuts import render
from .models import Anonce

def anonce_list_view(request):
    qs=Anonce.objects.all()
    context={
        'qs':qs

    }
    return render(request,'anonce/Announcement.html',context)
