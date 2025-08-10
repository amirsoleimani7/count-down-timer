from django.shortcuts import render
from django.utils import timezone
from .models import Event


def countdown_timer(request):
    
    event = Event.objects.first()

    if event:
        time_remainng = event.event_date - timezone.now()
        hours = time_remainng.seconds // 3600
        minuts = (time_remainng.seconds % 3600) // 60
        seconds = (time_remainng.seconds % 60)
        
        data = {
            'name' : event.name ,
            'hours'  : hours , 
            'minutes'  :minuts , 
            'seconds' : seconds ,
        }

    else : 
        data =  {
            'name' : "No Event" , 
            'hours'  : 0 , 
            'minutes'  :0 , 
            'seconds' : 0 ,
        }
    

    context = {
        'data' : data
    }
    
    return render(request,  'home/myapp.html' , context)