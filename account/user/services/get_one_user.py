from rest_framework import status
from rest_framework.response import Response
from ..model import User
from ..serializers import UserSerializer


def get_one_user(user_id):
    try:
        user_info = User.objects.get(user_id=user_id)
        serializers = UserSerializer(user_info)
        return Response(serializers.data)

    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)