from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from products.models import Product, Comment, Blog


class LandingPageView(View):
    def get(self, request):
        search = request.GET.get('search')
        products = Product.objects.all()
        comments = Comment.objects.all()
        blogs = Blog.objects.all()
        context = {
            'products': products,
            'search': search,
            'comments': comments,
            'blogs': blogs,
        }
        if not search:
            return render(request, 'index.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)

            if products:
                return render(request, 'index.html', context)

            else:
                return render(request, 'index.html', context)


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            # Add error handling here for password mismatch
            return render(request, 'auth/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            # Add error handling here for existing user
            return render(request, 'auth/register.html', {'error': 'Username already exists'})

        user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        user.set_password(password_1)
        user.save()
        return redirect('login')


class UserLoginView(View):
    def get(self, request):
        forms = AuthenticationForm()
        return render(request, 'auth/login.html', {'form': forms})

    def post(self, request):
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request, user)
            return redirect('landing')

        return render(request, 'auth/login.html', {'forms': forms})


class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("landing")


