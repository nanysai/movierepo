from django.shortcuts import render
from testapp.forms import Movieform
from testapp.models import Movie

# Create your views here.
def mov(request):
    return render(request,'testapp/movie.html')

def add(request):
    if request.method=='POST':
        obj=Movieform(request.POST)
        if obj.is_valid():
            print('all are validating')
            obj.save()
    obj=Movieform()
    dict={'obj':obj}
    return render(request,'testapp/add.html',dict)

def list(request):
    obj=Movie.objects.all()
    dict={'obj':obj}
    return render(request, 'testapp/list.html', dict)
