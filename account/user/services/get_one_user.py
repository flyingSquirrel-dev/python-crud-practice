from ..model import User
from ..serializers import UserSerializer


def get_one_user(user_id):
    global serializers, http_status_code

    try:
        user_info = User.objects.get(user_id=user_id)
        serializers = UserSerializer(user_info)
        http_status_code = 200

    except User.DoesNotExist:
        # TODO: 검색한 user_id가 없는 경우, 403 맞나?
        http_status_code = 403

    return [http_status_code, serializers]
