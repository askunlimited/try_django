from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_view(request):
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    
    return render(request, 'accounts/register.html', {"form": form })



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user=user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {"form": form}

    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "accounts/logout.html", {})

# def logout_view(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect("login")
#     return redirect("login")


# def register_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
    
#     return render(request, "accounts/register.html")


