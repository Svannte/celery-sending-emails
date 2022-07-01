from django.shortcuts import render
from django.views.generic import ListView
from .forms import MessageForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


# Create your views here.


class MessageEmailView(FormView):
    template_name = 'emails/message.html'
    form_class = MessageForm

    def form_valid(self, form):
        form.send_email()
        msg = "Message was sent"
        return HttpResponse(msg)
