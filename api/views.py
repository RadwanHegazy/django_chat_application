from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from frontend.models import Room, User
from .models import Message


@csrf_exempt
def send_msg (request) :

    user_id = request.COOKIES.get('user')
    room_id = request.COOKIES.get('last_room')
    # user_id = request.POST['userid']
    # room_id = request.POST['roomid']

    user = User.objects.get(id=user_id)
    room = Room.objects.get(id=room_id)


    if 'msg' in request.POST :
        msg = request.POST['msg']
        Message.objects.create(
            room = room,
            sender = user,
            body = msg
        )

    elif 'image' in request.FILES :
        image = request.FILES['image']
        print(request.FILES)
        Message.objects.create(
            room = room,
            sender = user,
            img = image
        )


    return HttpResponse('ok')




def all_msgs (request) :

    room_id = request.GET['roomid']
    room = Room.objects.get(id=room_id)

    msgs_in_list = []
    msgs = Message.objects.filter(room=room).order_by('date')

    for i in msgs :
        data = {
            'sender':i.sender.user,
            'date':i.date.date(),
        }

        if i.body :
            data['body'] = i.body
        
        elif i.img :
            data['img'] = i.img.url
        
        msgs_in_list.append(data)
        
    return JsonResponse(data=msgs_in_list,safe=False)
    