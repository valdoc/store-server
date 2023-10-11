from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm

from products.models import Basket
from users.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = "Store - Авторизация"


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы зарегистрированы'
    title = 'Store - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Профиль'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context
