from django.shortcuts import render, redirect

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
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'baseapp/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'baseapp/room_form.html', context)


