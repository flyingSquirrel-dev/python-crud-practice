from django.urls import path, include
from django.conf.urls import url
from . import views
from .services.user_view import UserView

urlpatterns = [
    path('users/', views.user_list),
    path('user/', views.create_an_user, name='create_user'),
    path('user/<str:user_id>', views.get_an_user),
    path('update_user/', views.update_an_user, name='update_user'),
    path('remove_user/', views.delete_an_user, name='delete_user'),
]

# TODO: 뒤에 slash 안 붙게하고 싶은데 잘 모르겠다
# urlpatterns = [
#     path('users/', views.user_list),
#     path('user/<str:user_id>', views.get_an_user),
#     url(r'^user/$', UserView.as_view(), name='user_view'),
# ]
