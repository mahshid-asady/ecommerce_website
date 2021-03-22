from django.shortcuts import render,redirect
from django.contrib.auth import login, get_user_model, authenticate, logout


# Create your views here.
from eshop_account.forms import LoginForm, RegisterForm

User = get_user_model()


def login_process(request):
    if request.user.is_authenticated:
        return redirect('/')

    Loginform= LoginForm(request.POST or None)
    if Loginform.is_valid():

        email = Loginform.cleaned_data.get('email')
        password = Loginform.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            Loginform.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
    context = {
        'login_form': Loginform
    }
    return render(request, 'login_page.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def logout_process(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')