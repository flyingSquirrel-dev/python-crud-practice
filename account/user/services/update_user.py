from rest_framework import status
from rest_framework.response import Response
from ..model import User
from ..serializers import UserSerializer


def update_user(request_dict):
    try:
        user_data = User.objects.get(user_id=request_dict['user_id'])
        serializer = UserSerializer(user_data, data=request_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
