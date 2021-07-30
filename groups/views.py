from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin, 
    PermissionRequiredMixin)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Group, GroupMember
from .forms import GroupMemberForm, CheckboxForm


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description") # these are the fields that show on the form. 
    model = Group
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'groups/group_list.html'

    # def def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["slug"] = Group.kwargs.get("slug")
    #     return context
    

    def post(self, request, *args, **kwargs):
        joinlist = request.POST.getlist('checks[]')
        print("here is the list")
        print(joinlist)
        # group = Group.objects.filter(pk=self.args.get(7))

        # GroupMember.objects.create(user=self.request.user,group=group)
        print(joinlist)
        for j in joinlist:
            # group = get_object_or_404(Group,name=self.kwargs.get(j))
            group = Group.objects.filter(pk=self.kwargs.get(j))
            print("test group")
            GroupMember.objects.create(user=self.request.user,group=group)
        return super().get(request, *args, **kwargs)
      

class JoinGroupList(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'groups/group_test.html'
    fields = ('user','group')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
            print("Your trying to join")
        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))
            print("warning")

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))
            print("You joined")
        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()
            print("Your trying to leave")
        except GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
            print("warning")
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
            print("you left the group")
        
        return super().get(request, *args, **kwargs)


# https://djangogirls.org/

# https://simpleisbetterthancomplex.com/

# Django Best Practices

# Model Query set
# Django rest framework

# Postman for testing