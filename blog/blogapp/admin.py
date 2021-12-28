from django.contrib import admin
from .models import PostBlog, Categories, UserProfile

admin.site.register(PostBlog)
admin.site.register(Categories)
admin.site.register(UserProfile)
