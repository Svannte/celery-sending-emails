from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegistrationForm
from .models import Account


# Create your models here.


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    """def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url"""

    def get_success_url(self):
        success_url = reverse('login')
        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['name', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('emails:home')

    def get_object(self, queryset=None):
        return self.request.user
