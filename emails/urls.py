from django.urls import path
from django.contrib.auth.views import TemplateView
app_name = "emails"

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
