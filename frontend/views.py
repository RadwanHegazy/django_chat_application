from django.shortcuts import render, redirect
from .models import Room, User

# Create your views here.


def register (request) :

    user = request.COOKIES.get('user')
    last_room_id = request.COOKIES.get('last_room')

    if user and last_room_id :
        get_room = Room.objects.get(id=last_room_id)
        return redirect('room',get_room.id)
    
    else :
        # add him to the last room 
        pass

    if request.method == 'POST' :
        user = request.POST['user']
        room = request.POST['room']
        
        user = User.objects.create(user=user)

        room , _ = Room.objects.get_or_create(name=room)
        
        if user in room.user.all() :
            res = redirect('room',room.id)
        else :
            room.user.add(user)
            room.save()
            res = redirect('room',room.id)
            
        res.set_cookie('user',user.id)
        res.set_cookie('last_room',room.id)
        
        return res
    
    res = render(request,'register.html')
    
    return res


def room (request,roomid) :
    
    get_room = Room.objects.get(id=roomid)
    user = User.objects.get(id=request.COOKIES.get('user'))
    
    return render(request,'room.html',{'room':get_room,'user':user})


def logout(request) :
    res = redirect('register')
    res.delete_cookie('user')
    res.delete_cookie('last_room')

    return res