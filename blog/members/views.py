from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChange, ProfilePageForm
from blogapp.models import UserProfile


class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = "registration/create_profile_page.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfilePageEditView(UpdateView):
    model = UserProfile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'profile_pic', 'linkedin_url', 'twitter_url', 'facebook_url']
    success_url = reverse_lazy('home')


class ProfilePageView(DetailView):
    model = UserProfile
    template_name = "registration/view_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data()
        user_info = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["user_info"] = user_info
        return context


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChange
    success_url = reverse_lazy('home')


class Registration(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
