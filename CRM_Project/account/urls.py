from django.urls import path

from account.views.change_temporary_password import ChangeTemporaryPasswordView
from account.views.login import LoginView
from account.views.logout import LogoutView
from account.views.password_reset import PasswordResetRequestView, PasswordResetConfirmView
from account.views.profile import UserRetrieveView
from account.views.set_new_password import SetNewPasswordView

app_name = 'account'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
    path('change-temporary-password/', ChangeTemporaryPasswordView.as_view(), name='change-temporary-password'),
    path('profile/', UserRetrieveView.as_view(), name='profile')

]
