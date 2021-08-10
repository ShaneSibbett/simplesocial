# simplesocial
This is an learning project. The concepts used here will be helpful to me else where.

#### My current challenge:
 I want to be able to have users see the list and click the checkboxes to join straight from the list page. I was able to get this the join group to work. The problem I need help with now is leaving the group. Below is the ListGroups class with join group (with in the simplesocial\groups\views.py)

class ListGroups(LoginRequiredMixin, generic.ListView): model = Group template_name = 'groups/group_list.html'

def post(self, request, *args, **kwargs):
    joinlist = request.POST.getlist('join[]')
    leavelist = request.POST.getlist('leave[]')
    print("here is the list")
    print(joinlist)
    print(leavelist)
    # group = Group.objects.filter(pk=self.args.get(7))
    user=self.request.user
    # GroupMember.objects.create(user=self.request.user,group=group)
    for j in joinlist:
        group = Group.objects.get(pk=j)
        print(user)
        print(group.name)
        GroupMember.objects.create(user=user,group=group)
    return super().get(request, *args, **kwargs)
For this to work it requires the Java script that is in the simplesocial\templates\base.html

<script>
  $(document).ready(function(){
    $('.checkboxclassname').click(function(){var txt="";
    $('.checkboxclassname:checked').each(function(){
      txt+=$(this).val()+","});
    $('#checkboxlist').val(txt);});
  });
</script>
The above base.html is inherited by other html files. The checkboxes show up on simplesocial\groups\templates\groups\group_list.html file.

The pip freeze results below. Sorry I don't have recall what items I am using in this project. 

argon2-cffi==20.1.0 
asgiref==3.4.1 
astroid==2.4.2 
async-generator==1.10 
attrs==20.3.0 
babelfish==0.5.5 
backcall==0.2.0 
bcrypt==3.2.0 
beautifulsoup4==4.9.3 
bleach==3.3.0 
certifi==2020.11.8 
cffi==1.14.5 
chardet==3.0.4 
colorama==0.4.4 
decorator==5.0.7 
defusedxml==0.7.1 
diff-match-patch==20200713 
Django==3.2.5 
django-bootstrap-v5==1.0.2 
django-braces==1.14.0 
django-crispy-forms==1.11.2 
django-extensions==3.1.2 
django-object-tools==2.0.0 
entrypoints==0.3 
et-xmlfile==1.0.1 
greenlet==1.0.0 
idna==2.10 
ipykernel==5.5.3 
ipython==7.22.0 
ipython-genutils==0.2.0 
ipywidgets==7.6.3 
isort==5.6.4 
jdcal==1.4.1 
jedi==0.18.0 
Jinja2==2.11.3 
jsonschema==3.2.0 
jupyter-client==6.1.12 
jupyter-core==4.7.1 
jupyterlab-pygments==0.1.2 
jupyterlab-widgets==1.0.0 
lazy-object-proxy==1.4.3 
MarkupPy==1.14 
MarkupSafe==1.1.1 
mccabe==0.6.1 
mistune==0.8.4 
nbclient==0.5.3 
nbconvert==6.0.7 
nbformat==5.1.3 
nest-asyncio==1.5.1 
notebook==6.3.0 
numpy==1.19.4 
odfpy==1.4.1 
openpyxl==3.0.6 
packaging==20.9 
pandas==1.1.4 
pandocfilters==1.4.3 
parso==0.8.2 
pickleshare==0.7.5 
prometheus-client==0.10.1 
prompt-toolkit==3.0.18 
pycparser==2.20 
Pygments==2.8.1 
pylint==2.6.0 
pyparsing==2.4.7 
pyrsistent==0.17.3 
python-dateutil==2.8.1 
pytz==2020.4 
pywin32==300 
pywinpty==0.5.7 
PyYAML==5.4.1 
pyzmq==22.0.3 
requests==2.25.0 
Send2Trash==1.5.0 
six==1.15.0 
soupsieve==2.2.1 
SQLAlchemy==1.4.13 
sqlparse==0.4.1 
tablib==3.0.0 
terminado==0.9.4 
testpath==0.4.4 
toml==0.10.2 
tornado==6.1 
traitlets==5.0.5 
urllib3==1.26.2 
wcwidth==0.2.5 
webencodings==0.5.1 
widgetsnbextension==3.5.1 
wrapt==1.12.1 
xlrd==2.0.1 xlwt==1.3.0