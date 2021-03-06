from django.urls import re_path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, new_invitation, accept_invitation

urlpatterns = [
    re_path(r'home$', home, name="player_home"),
    re_path(r'login$',
            LoginView.as_view(template_name="player/login_form.html"),
            name="player_login"),
    re_path(r'logout$',
            LogoutView.as_view(),  # convert to function, in a class based view
            name="player_logout"),  # name
    re_path(r'new_invitation$', new_invitation, name="player_new_invitation"),
    # matches one or more digits eg. accept_invitations/12/
    re_path(r'accept_invitations/(?P<id>\d+)/$',
            accept_invitation,
            name="player_accept_invitation")
]
