from rest_framework import status
from rest_framework.response import Response
from ..model import User


def delete_user(user_id):
    try:
        user_data = User.objects.get(user_id=user_id)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
