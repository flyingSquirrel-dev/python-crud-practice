from ..model import User
from ..serializers import UserSerializer


def create_user(request_dict):
    global http_status_code
    try:
        User.objects.get(user_id=request_dict['user_id'])
        http_status_code = 409
    except User.DoesNotExist:
        created_user_info = UserSerializer(data=request_dict)
        if created_user_info.is_valid():
            created_user_info.save()
            http_status_code = 201
        elif not created_user_info:
            http_status_code = 500

    return http_status_code
