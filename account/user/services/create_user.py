from rest_framework import status
from rest_framework.response import Response
from ..model import User
from ..serializers import UserSerializer


def create_user(request_dict):
    try:
        User.objects.get(user_id=request_dict['user_id'])
        return Response(status=status.HTTP_409_CONFLICT)
    except User.DoesNotExist:
        created_user_info = UserSerializer(data=request_dict)
        if created_user_info.is_valid():
            created_user_info.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
