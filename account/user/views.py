from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import (
    get_all_users,
    get_one_user,
    create_user,
    update_user,
    delete_user
)


@api_view(['GET'])
def user_list(request):
    users_data = get_all_users()
    return Response(users_data)


@api_view(['GET'])
def get_an_user(request, user_id):
    http_status_code, serializers = get_one_user(user_id)

    if http_status_code == 403:
        return Response(status=status.HTTP_403_FORBIDDEN)
    elif http_status_code == 200:
        return Response(serializers.data)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_an_user(request):
    http_status_code = create_user(request.data)
    if http_status_code == 409:
        return Response(status=status.HTTP_409_CONFLICT)
    elif http_status_code == 201:
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_an_user(request):
    http_status_code = update_user(request.data)
    if http_status_code == 403:
        return Response(status=status.HTTP_403_FORBIDDEN)
    elif http_status_code == 400:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif http_status_code == 200:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_an_user(request):
    http_status_code = delete_user(request.data['user_id'])
    print('http_status_code', http_status_code)
    if http_status_code == 403:
        return Response(status=status.HTTP_403_FORBIDDEN)
    elif http_status_code == 204:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
