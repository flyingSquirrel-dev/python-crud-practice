from ..model import User
from ..serializers import UserSerializer


def get_all_users():
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return serializer.data
