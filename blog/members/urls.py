from django.urls import path
from .views import Registration, UserEdit, ChangePasswordView, ProfilePageView, ProfilePageEditView, ProfileCreateView

urlpatterns = [
    path('register/', Registration.as_view(), name="register"),
    path('edit_profile/', UserEdit.as_view(), name="edit_profile"),
    path('password/', ChangePasswordView.as_view(template_name="registration/change_password.html")),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile/', ProfilePageEditView.as_view(), name="edit_profile_page"),
    path('create_profile/', ProfileCreateView.as_view(), name="create_profile_page"),
]
