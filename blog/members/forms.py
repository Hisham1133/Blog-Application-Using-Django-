from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'style': 'max-width: 300px;'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'style': 'max-width: 300px;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'style': 'max-width: 300px;'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'max-width: 300px;'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['style'] = 'max-width: 300px;'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['style'] = 'max-width: 300px;'


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'style': 'max-width: 300px;'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'style': 'max-width: 300px;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'style': 'max-width: 300px;'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'style': 'max-width: 300px;'}))

    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                                            'style': 'max-width: 300px;'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check',
    #                                                                                  'style': 'max-width: 300px;'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check',
    #                                                                              'style': 'max-width: 300px;'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check',
    #                                                                               'style': 'max-width: 300px;'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                                             'style': 'max-width: 300px;'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                     'style': 'max-width: 300px;'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                      'style': 'max-width: 300px;'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                      'style': 'max-width: 300px;'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChange, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = "New Password"
        self.fields['new_password2'].label = "Confirm Password"
