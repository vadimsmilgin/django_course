from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.


class Main(TemplateView):
    template_name = "main.html"

    def get(self, request):
        return render(request, self.template_name, {})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "acc/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
        pass


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    template_name = "acc/reg.html"
    success_url = "login.html"

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)
        pass


class LogoutFormView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
        pass