from django.urls import path
from .views import Registration, UserEdit

urlpatterns = [
    path('register/', Registration.as_view(), name="register"),
    path('edit_profile/', UserEdit.as_view(), name="edit_profile"),
]
