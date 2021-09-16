from django.shortcuts import render
from .models import Attend
from django.utils import timezone

# Create your views here.

def attend_view(request):
    status = None
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                attended_datetime = str(timezone.now())[:10]
                print(attended_datetime)
            except:
                pass

            attended_today = Attend.objects.filter(attender=request.user, datetime__startswith=attended_datetime)
            
            if str(attended_today)[10:] == "[]>":
                status = 3

            else:
                status = 2

            if status == 3:
                attend_object = Attend(attender=request.user)
                attend_object.save()
                status= 1

        else: 
            status = 0
    return render(request, "main_app/attend.html", {'status': status})