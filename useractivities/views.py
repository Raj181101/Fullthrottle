from django.shortcuts import render
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse
from useractivities.models import *
# Create your views here.


class UserSerializer(ModelSerializer):
    activity_periods = SerializerMethodField()

    class Meta:
        model = User
        depth = 1
        fields = ('id','real_name','tz','activity_periods')
    
    def get_activity_periods(self, user):       
        context = []
        activities = user.activityperiods_set.all()
        for activity in activities:
            data = {}
            data['start_time'] = activity.start_time.strftime('%b %d %Y %I:%M %p')
            data['end_time'] = activity.end_time.strftime('%b %d %Y %I:%M %p')
            context.append(data)
        
        return context


@require_GET
@csrf_exempt
def users(request):
    '''
        url = 'http://127.0.0.1:8000/api/users/'
    '''

    
    try:
        users = User.objects.all()
        status = True
        response = UserSerializer(users, many=True).data

    except ValidationError:
        status = False
        data = ["Something went wrong"]

    return JsonResponse({
            'ok' : status,
            'members' : response
        })