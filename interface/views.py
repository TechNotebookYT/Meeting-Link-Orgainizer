from django.shortcuts import render
from datetime import datetime
from .models import Link

# Create your views here.
def current_meeting(request):
    current_time = datetime.now()

    current_hour = current_time.hour #3:00 pm -> 15
    current_min = current_time.minute #3:00 pm -> 0

    meeting_list = list(Link.objects.all())
    # final_meeting = [] <- DELETE THIS LINE
    current_meeting = None

    def time_in_mins(hr, min):
        return hr * 60 + min

    for meeting in meeting_list:
        start_time_hour = meeting.start_time.hour
        start_time_min = meeting.start_time.minute

        end_time_hour = meeting.end_time.hour
        end_time_min = meeting.end_time.minute

        day_list = []

        if meeting.monday == True:
            day_list.append('Monday')
        if meeting.tuesday == True:
            day_list.append('Tuesday')
        if meeting.wednesday == True:
            day_list.append('Wednesday')
        if meeting.thursday == True:
            day_list.append('Thursday')
        if meeting.friday == True:
            day_list.append('Friday')

        if ((day_list.count(current_time.strftime('%A')) == 0)
            or (time_in_mins(start_time_hour, start_time_min) - 6) > time_in_mins(current_hour, current_min)
                or (time_in_mins(end_time_hour, end_time_min)) < time_in_mins(current_hour, current_min)):
            continue
        
        current_meeting = meeting

    if current_meeting == None:
        return render(request, 'nomeetings.html')
    else:
        return render(request, 'linktoclick.html', {'obj': current_meeting})


        
        



    

