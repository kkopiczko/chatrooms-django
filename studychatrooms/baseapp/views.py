from django.shortcuts import render

# Create your views here.

from .models import Room

# rooms = [
#     {
#         'id': 1,
#         'name': 'Let\'s learn python'
#     },
#     {
#         'id': 2,
#         'name': 'Javascript'
#     },
#     {
#         'id': 3,
#         'name': 'Spaghetti fans'
#     }
# ]

def home(req):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(req, 'baseapp/home.html', context)

def room(req, pk):
    # for r in rooms:
    #     if r['id'] == int(pk):
    #         room = r
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(req, 'baseapp/room.html', context)

