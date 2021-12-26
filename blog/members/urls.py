from django.urls import path
from .views import Registration, UserEdit, ChangePasswordView

urlpatterns = [
    path('register/', Registration.as_view(), name="register"),
    path('edit_profile/', UserEdit.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(template_name="registration/change_password.html"))
]
