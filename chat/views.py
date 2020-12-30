from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

def index(request):
    if request.method == 'POST':
        userform = NameForm(request.POST)
        roomname=userform.data['roomname']
        print(userform.data)
        return render(request, 'chatroom.html', {
        'room_name': roomname
    })
    else:
        myform = NameForm()
        return render(request, 'index.html', {'form': myform})

