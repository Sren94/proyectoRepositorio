from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView
from .models import User
from .forms import userRegisterForm, LoginForm,UpdateUserForm
from django.views.generic import (FormView,View)
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

class UserCreateView(FormView):
    model = User
    template_name = "user/registerUser.html"
    form_class=userRegisterForm
    success_url='/'
    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            firstName=form.cleaned_data['firstName'],
            lastName=form.cleaned_data['lastName'],
        )
        return super(UserCreateView,self).form_valid(form)
    

class Panel(LoginRequiredMixin,TemplateView):
    login_url= reverse_lazy('user_app:login')
    template_name = "user/Panel.html"

class LoginUser(FormView):
    template_name='user/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('user_app:panel')
    def form_valid(self, form):
        user=authenticate(
            username=form.cleaned_data['userName'],
            password=form.cleaned_data['password']
        )
        login(self.request,user)
        return super(LoginUser,self).form_valid(form)

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )
        )

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = "user/updateUser.html"
    success_url=reverse_lazy('user_app:panel')
    form_class= UpdateUserForm
    
    def form_valid(self, form):
        print('Metodo Self')
        return super().form_valid(form)

