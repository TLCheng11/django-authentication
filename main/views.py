from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import PostForm, RegistrationForm
from .models import Post


# Create your views here.
# To redirect if user is not login
@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        # get the value from the named button
        post_id = request.POST.get("delete-post-id")
        post = Post.objects.get(id=post_id)

        # check if post exist and if author is the user
        if post and post.author == request.user:
            post.delete()

    return render(request, 'main/home.html', {"posts": posts})

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})

@login_required(login_url="/login")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # commit=False means don't add to database yet
            post = form.save(commit=False)
            # link the user to the post, then save
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, "main/create_post.html", {"form": form})