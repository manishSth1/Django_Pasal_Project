from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm


class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('product-home-page')
        return render(request, 'user/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request=request, user=user)
            return redirect('product-home-page')
        context={
            'message': 'Invalid Credentials'
        }
        return render(request, 'user/login.html', context=context, status=404)

class SignupView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('product-home-page')
        context = {
            'form': SignupForm()
        }
        return render(request, 'user/signup.html', context=context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-home-page')
        else:
            context = {
                'form': SignupForm(initial=request.POST.dict()), 
                'message': form.errors,
            }
        return render(request, 'user/signup.html', context=context)   

def log_out_view(request):
    user: User = request.user
    if request.method == 'POST' and user.is_authenticated:
        logout(request)
    return redirect('product-home-page')
    





# class LogoutView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             logout(request)
#         return render(request, 'user/logout.html')


        