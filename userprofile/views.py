from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.contrib.auth.models import User
from .models import Profile

from .forms import UserForm, ProfileForm


class UserList(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/index.html'


class UserDetail(DetailView):
    model = User
    template_name = 'users/user_detail.html'

    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserEdit(UpdateView):
    """
    Menampilkan models user dan profile form dalam satu page - edit user
    """
    model = User
    second_model = Profile
    
    form_class = UserForm
    second_form_class = ProfileForm

    template_name = 'users/user_edit.html'

    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserEdit, self).get_context_data(**kwargs)
        context['second_form'] = ProfileForm

        profile_object = self.second_model.objects.get(user__username=self.kwargs.get('username'))
        profile_form = self.second_form_class(instance=profile_object, prefix='profiles')

        context['profile_form'] = profile_form
        return context

    def get_success_url(self):
        return reverse('user-detail', kwargs={'username': self.kwargs.get('username')})

    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        instance_user = User.objects.get(username=self.kwargs.get('username'))
        instance_profile = Profile.objects.get(user=instance_user)
        form = self.form_class(request.POST, instance=instance_user)
        profile_form = self.second_form_class(request.POST, prefix='profiles', instance=instance_profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form, profile_form)