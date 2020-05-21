from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from groups.models import Group, GroupMember
from django.shortcuts import get_object_or_404

class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ["name", "description"]
    model = Group
    template_name = "groups/group_form.html"

class SingleGroup(DetailView):
    model = Group
    template_name = "groups/group_detail.html"

    slug_field = "slug"
    slug_url_kwargs = "group_slug"

class ListGroups(ListView):
    model = Group
    template_name = "groups/group_list.html"


class JoinGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs['slug']})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs['slug'])

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, "You are already a member!")
        else:
            messages.success(self.request, "You are now a member!")
        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = (models
                          .GroupMember.object
                          .filter(user=self.request.user, group__slug=self.kwargs['slug'])
                          .get())
        except:
            messages.warning(self.request, "You are not in the group")
        else:
            membership.delete()
            messages.success(self.request, "you have left the group")

        return super().get(request, *args, **kwargs)
