from django.forms import ModelForm
from Userdetail.models import *
from django  import forms

class Usercreateform(ModelForm):
    Confirmpassword = forms.CharField(max_length=200, widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'Password': forms.PasswordInput(render_value=True),
        }
        model = Users
        fields = ["Name", "Telephone", "Email", "Username", "Password","Confirmpassword"]
    def clean(self):
        cleaned_data=super().clean() #mandatory
        Name=cleaned_data.get("Name")
        Telephone=cleaned_data.get("Telephone")
        Email=cleaned_data.get("Email")
        Username=cleaned_data.get("Username")
        Password=cleaned_data.get("Password")
        Confirmpassword=cleaned_data.get("Confirmpassword")

        if Password!=Confirmpassword:
            msg="Pls enter a valid password"
            self.add_error("Password",msg)

class Userlogin(forms.Form):
    Username=forms.CharField(max_length=200,)
    Password=forms.CharField(max_length=200, widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'Password': forms.PasswordInput(render_value=True),
        }
        model=Users
        fields=['Username','Password',]

    def clean(self):
        cleaned_data=super().clean() #mandatory
        Username = cleaned_data.get("Username")
        # print(Username)
        # qs=Users.objects.get(Username==Username)
        # print("sss",qs.Username)
        # Password = cleaned_data.get("Password")
        # if(Users.objects.get(Username==Username)):
        #     print(Username)
        #     pass
        # else:
        #     msg="No user exist in this name"
        #     self.add_error('Username',msg)