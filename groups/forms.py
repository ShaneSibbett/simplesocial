from django import forms
# from django.forms import ModelForm
from .models import Group, GroupMember


class GroupMemberForm(forms.ModelForm): # this PostForm inherits from the ModelForm

    # class Meta:
    #     fields = ('group', 'user')
    #     model = models.GroupMember
    # group = forms.CharField(max_length=40, label='Group name')
    # user = forms.CharField(max_length=40, label='The username')
    # joingroup = forms.ModelMultipleChoiceField(queryset = Group.objects.all(), widget  = forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        group_list = kwargs.pop('group_list', None)
        super(GroupMemberForm, self).__init__(*args, **kwargs)
        self.fields['group'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=group_list)
        for i, q in enumerate(Group.objects.all()):
            self.fields['%s_field' % i] = forms.BooleanField()
        
        self.fields["group"].queryset = (
                Group.objects.filter(pk__in=user.groups.values_list("group__pk")))


class CheckboxForm(forms.Form): # this PostForm inherits from the ModelForm
    getcheck = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input', 'type':'checkbox', 'name':'jb_1', 'id':'1' }))
    text = forms.CharField()

class JoinGroupForm(forms.ModelForm):
    def __init__(self, userlist, *args, **kwargs):
        self.custom_fields = userlist
        super(forms.Form, self).__init__(*args, **kwargs)
        for f in userlist:
            self.fields[str(f.id)] = forms.BooleanField(initial=False)    

    def get_selected(self):
        """returns selected users"""
        return filter(lambda u: self.fields[str(u.id)], self.custom_fields)
