from django import forms
from.models import PostBlog, Categories


class PostBlogForms(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ('title', 'author', 'category', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of your blog'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }


class UpdateBlogForms(forms.ModelForm):
    class Meta:
        model = PostBlog
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title of your blog'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }