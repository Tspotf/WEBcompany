from django.shortcuts import render
from  django.http import HttpResponse
from .forms import EventForm
from .models import Event
from django.utils.dateparse import parse_date
from .models import Employee

def all_events(request):
    query_date=request.GET.get('date')
    if query_date:
        date=parse_date(query_date)
        events=Event.objects.filter(date=date)
    else:
        events=Event.objects.all()
    return render(request,'all_events.html',{'events':events})


def home(request):
    return render(request,'home.html')


def employee_detail(request,employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employee.html', {'employee': employee})



def create_events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            print(Event.objects.all())
    else:
        form = EventForm
    return render(request, 'event.html', {'form': form})

def all_employee(request):
    query_date=request.GET.get('date')
    if query_date:
        date=parse_date(query_date)
        employee=Employee.objects.filter(date=date)
    else:
        employee=Employee.objects.all()
    return render(request,'all_employee.html',{'employee':employee})


# def all_events(request):
#     events=Event.objects.all()
#     return render(request, 'all_events.html', {'events':events})







