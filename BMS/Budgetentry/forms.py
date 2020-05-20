from django.forms import ModelForm
from Userdetail.models import *
# from Userdetail.views import *
from Budgetentry.models import *
from django  import forms
# from django.shortcuts import *
# from django.views.generic import *
# from django.urls import *
from django.forms import ModelChoiceField
class DateInput(forms.DateInput):
    input_type = 'date'
class Addaccountform(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Addaccountform, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['Username1'].widget.attrs['readonly'] = True
    class Meta:
        model = Account
        fields = ["Paymode",]


        def clean(self):
            cleaned_data=super().clean() #mandatory
            Paymode=cleaned_data.get("Paymode")
            # Username = request.session['Username']
            # Username = cleaned_data.get("Username")
            # Username1= request.session['Username']
class Addessentialform(ModelForm):

    class Meta:
        model=Essential
        fields=['Category',]
        def clean(self):
            cleaned_data = super().clean()
            Category = cleaned_data.get("Category")
class MenuModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "Menu #%s) %s" % (obj.id,obj.name)

class Addentryform(ModelForm):
    Paymode = forms.MultipleChoiceField()
    # Username = forms.CharField(max_length=200, )

    # def __init__(self, *args, **kwargs):
    #     super(Addentryform, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['Username'].widget.attrs['readonly'] = True

    # Username = request.session["Username"]
    # Paymode = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True)
    def __init__(self, Username, *args, **kwargs):
        super(Addentryform, self).__init__(Username, **kwargs)
        self.fields['Paymode'].queryset = Account.objects.filter(Username=Username)
        # return None
        return self.fields['Paymode']
        # return None
        # Paymode_choices = [(Paymode.id, Paymode.Paymode) for Paymode in self.fields['Paymode'].queryset]
        # self.fields['Paymode'].choices = Paymode_choices
        # self.fields['Paymode'].widget = forms.CheckboxSelectMultiple()
        # self.fields['Paymode'].choices = self.fields['Paymode'].queryset
        print("--------------")
    class Meta:

        model=Entry
        # Paymode = MenuModelChoiceField(queryset=)
        # Paymode = forms.ModelMultipleChoiceField(queryset=None)
        fields=['Paymode','Category','Amount','Dfield']
        widgets = {
            'Dfield': DateInput(),
            # 'Paymode':Account.objects.filter(Username=request.session['Username']),
        }

        def clean(self):
            cleaned_data = super().clean()  # mandatory
            # Paymode = cleaned_data.get("Paymode")
            Category = cleaned_data.get("Category")
            Amount = cleaned_data.get("Amount")
            Dfield = cleaned_data.get("Dfield")
            print("a1a1a1")





    # print("a1a1a1")



class Addcategorywiseform(ModelForm):

    class Meta:
        model=Entry
        fields=['Category',]
        def clean(self):
            cleaned_data = super().clean()
            Category = cleaned_data.get("Category")



class Adddatewiseform(ModelForm):
    print("ddd")
    Startdate = forms.CharField(widget=DateInput)
    Enddate = forms.CharField(widget=DateInput)

    class Meta:
        model=Entry
        fields=['Category','Startdate','Enddate',]
        widgets = {
            'Startdate': DateInput(),
            'Enddate': DateInput(),
        }
        def clean(self):
            cleaned_data = super().clean()
            print("d error")
            Category = cleaned_data.get("Category")
            Startdate = cleaned_data.get("Startdate")
            Enddate = cleaned_data.get("Enddate")