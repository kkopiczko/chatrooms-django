from django.shortcuts import render

# Create your views here.

rooms = [
    {
        'id': 1,
        'name': 'Let\'s learn python'
    },
    {
        'id': 2,
        'name': 'Javascript'
    },
    {
        'id': 3,
        'name': 'Spaghetti fans'
    }
]

def home(req):
    context = {'rooms': rooms}
    return render(req, 'baseapp/home.html', context)

def room(req, pk):
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    context = {'room': room}
    return render(req, 'baseapp/room.html', context)

