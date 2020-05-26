from django.http import HttpResponse
from rest_framework.views import APIView
from ..model import User
from ..serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        # <view logic>
        print('get요청')
        return HttpResponse('result')
    def post(self, request):
        # <view logic x2>
        print('post요청')
        return HttpResponse('message_post_template')