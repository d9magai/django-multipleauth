from __future__ import absolute_import

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.models import Owner

from .forms import LoginForm


def is_owner(owner):
    return isinstance(owner, Owner)


class LoginView(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('owner:index')
    template_name = 'owner/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


@login_required(login_url=reverse_lazy('owner:login'))
@user_passes_test(is_owner, login_url=reverse_lazy('owner:login'))
def index(request):
    return render(request, 'owner/index.html')
