from django.shortcuts import render
from.models import Place
from.models import Team

#creat your views thrg
def environment(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request, 'index.html', {'result':obj, 'results':obj1})