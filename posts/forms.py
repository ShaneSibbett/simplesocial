from django import forms

from posts import models


class PostForm(forms.ModelForm): # this PostForm inherits from the ModelForm
    class Meta:
        fields = ("message", "group")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None) # if kwargs has no key 'user', user is assigned None
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (
                models.Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )
