from django.shortcuts import render

# Create your views here.

from .models import Room
from .forms import RoomForm
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

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'baseapp/home.html', context)

def room(request, pk):
    # for r in rooms:
    #     if r['id'] == int(pk):
    #         room = r
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'baseapp/room.html', context)

def create_room(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'baseapp/room_form.html', context)

