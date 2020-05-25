from ..model import User
from ..serializers import UserSerializer


def update_user(request_dict):
    global http_status_code
    try:
        user_data = User.objects.get(user_id=request_dict['user_id'])
        serializer = UserSerializer(user_data, data=request_dict)
        if serializer.is_valid():
            serializer.save()
            http_status_code = 200
        else:
            http_status_code = 400

    except User.DoesNotExist:
        http_status_code = 403

    return http_status_code
