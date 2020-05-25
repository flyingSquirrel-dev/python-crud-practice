from rest_framework.decorators import api_view
from .services import (
    get_all_users,
    get_one_user,
    create_user,
    update_user,
    delete_user
)


@api_view(['GET'])
def user_list(request):
    return get_all_users()


@api_view(['GET'])
def get_an_user(request, user_id):
    return get_one_user(user_id)


@api_view(['POST'])
def create_an_user(request):
    return create_user(request.data)


@api_view(['PUT'])
def update_an_user(request):
    return update_user(request.data)


@api_view(['DELETE'])
def delete_an_user(request):
    return delete_user(request.data['user_id'])
