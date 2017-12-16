from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.views.generic import FormView, RedirectView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

class LoginView(FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'home/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')

class HomeView(TemplateView):
    template_name = "home/blank.html"

class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
