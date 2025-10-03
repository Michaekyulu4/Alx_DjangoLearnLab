from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login as auth_login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # optional: automatically log user in after registration
            auth_login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    # Display and update profile
    if request.method == "POST":
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        pform = ProfileForm(instance=request.user.profile)
    return render(request, "registration/profile.html", {"pform": pform})
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "blog/posts_list.html"   # template path
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 10  # optional

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    # redirect to login if not authenticated
    login_url = "login"

    def form_valid(self, form):
        # automatically set the author from the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    login_url = "login"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("posts")
    login_url = "login"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user