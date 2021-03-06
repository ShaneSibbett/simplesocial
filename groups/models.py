from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User

# import misaka # not in use

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")
    #methods
    def __str__(self): # string representation returns the name of the group
        return self.name

    def save(self, *args, **kwargs): # this creates a slugified name of the group
        self.slug = slugify(self.name)
        # self.description_html = misaka.html(self.description)
        self.description_html = self.description
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


class GroupMember(models.Model): # this creates the through table. It is used by the many to many. 
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_groups')
    # the below reterns the username
    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
