from ..model import User
from ..serializers import UserSerializer


def delete_user(user_id):
    global http_status_code
    try:
        user_data = User.objects.get(user_id=user_id)
        user_data.delete()
        http_status_code = 204
    except User.DoesNotExist:
        http_status_code = 403

    return http_status_code
