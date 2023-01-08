from django.urls import path, include

from accounts.views import CustomLogin, CustomPasswordChangeView, Registration

urlpatterns = [
    path("login/", CustomLogin.as_view(), name='login'),
    path("password_change/", CustomPasswordChangeView.as_view(), name='password_change'),
    # path("logout/", logout_view, name='logout'),
    path("registration/", Registration.as_view(), name='registration'),
    path('', include('django.contrib.auth.urls'))
]
