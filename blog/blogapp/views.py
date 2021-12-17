from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PostBlog, Categories
from .forms import PostBlogForms, UpdateBlogForms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = PostBlog
    template_name = "home.html"
    context_object_name = "list_items"
    # ordering = ['-id']
    ordering = ['-blog_published_date']

    def get_context_data(self, *args, **kwargs):
        cat_data = Categories.objects.all()
        context = super(HomeView, self).get_context_data()
        context["cat_data"] = cat_data
        return context


class BlogDetailsView(DetailView):
    model = PostBlog
    template_name = "blog_details.html"
    context_object_name = "item"

    def get_context_data(self, *args, **kwargs):
        blog_data = get_object_or_404(PostBlog, id=self.kwargs['pk'])
        total_likes = blog_data.total_likes()
        liked = False
        if blog_data.likes.filter(id=self.request.user.id).exists():
            liked = True
        cat_data = Categories.objects.all()
        context = super(BlogDetailsView, self).get_context_data()
        context["cat_data"] = cat_data
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class CreateBlogView(CreateView):
    model = PostBlog
    form_class = PostBlogForms
    template_name = "add_blog.html"

    def get_context_data(self, *args, **kwargs):
        cat_data = Categories.objects.all()
        context = super(CreateBlogView, self).get_context_data()
        context["cat_data"] = cat_data
        return context


class UpdateBlogView(UpdateView):
    model = PostBlog
    template_name = "update_blog.html"
    form_class = UpdateBlogForms
    context_object_name = "item"


class DeleteBlogView(DeleteView):
    model = PostBlog
    template_name = "delete_blog.html"
    context_object_name = "item"
    success_url = reverse_lazy("home")


class CreateCategories(CreateView):
    model = Categories
    template_name = "add_category.html"
    fields = '__all__'


def CategoryBlogView(request, cats):
    category_id = [category_id[0] for category_id in Categories.objects.filter(name=cats.replace("-", " ")).values_list(
        'id') if category_id]
    category_blogs = []
    if category_id:
        category_blogs = [blogs for blogs in PostBlog.objects.filter(category=category_id[0])]
    return render(request, 'blogs_under_category.html',
                  {'cats': cats.replace("-", " "), 'category_blogs': category_blogs})


def LikePostView(request, pk):
    post = get_object_or_404(PostBlog, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog_details', args=[str(pk)]))