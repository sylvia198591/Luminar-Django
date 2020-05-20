from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from Budgetentry.models import *
from Budgetentry.forms import *
from plotly.offline import plot
from plotly.graph_objs import Scatter
# import plotly.graph_objs as Scatter
import plotly.graph_objs as go
import plotly.graph_objects as go
# from Userdetail import views
# Create your views here.
# import plotly.express as px
from django.db.models import *
# from django.db.models import Sum
# USER=request.session['Username']
class createAccount(TemplateView):
    form_class=Addaccountform
    model_name=Account
    template_name = "Budgetentry/createAccount.html"
    # if(request.session.is_empty()):
    #     print("ddd")

    def get(self,request,*args,**kwargs):
        # Username=request.session['Username']
        context={}
        # context["Paymode"]=Account.objects.filter(Username=Username)
        context["form"]=self.form_class

        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("0000")

        if form.is_valid():
            print("11111")
            Paymode = form.cleaned_data["Paymode"]
            Username=request.session["Username"]
            print("sess:",request.session["Username"])
            print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs =Account.objects.create(Paymode=Paymode, Username=Username)
            print("d1")
            # form.save()
            print("d2")
            qs.save()
            print("d3")
            return redirect("Account_view")
        else:
            return render(request, self.template_name,{"form":form})


class viewAccount(TemplateView):
    model_name=Account
    template_name = "Budgetentry/viewAccount.html"
    # Username = request.session["Username"]
    # def get_queryset(self):
    #
    #     return self.model_name.objects.filter(Username=request.session["Username"])
    def get(self, request, *args, **kwargs):
        # form.fields['Paymode'].queryset = Account.objects.filter(Username=request.session["Username"])
        qs=Account.objects.filter(Username=request.session["Username"])
        print("ddddd")
        context={}
        context["viewaccount"]=qs
        return render(request,self.template_name,context)

class updateAccount(UpdateView):
    model=Account
    fields = ['Paymode',]
    success_url = '/Viewaccount'
    # success_url = reverse_lazy('getRes')
    #context_object_name = "form"
    template_name = 'Budgetentry/createAccount.html'
class deleteAccount(DeleteView):
    model = Account
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    fields = ['Paymode']
    # template_name_suffix = "_del"
    success_url = '/Viewaccount'

# class updateAccount(UpdateView):
#     model = Account
#     fields = ['Paymode']
#     template_name_suffix = "_update"
#     success_url = '/Viewaccount'

class createEssential(TemplateView):
    form_class=Addessentialform
    model_name=Essential
    template_name = "Budgetentry/createEssential.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("0000")
        if form.is_valid():
            print("11111")
            Category = form.cleaned_data["Category"]
            Username=request.session["Username"]
            print("sess:",request.session["Username"])
            print("cat:",Category)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs =Essential.objects.create(Category=Category, Username=Username)
            print("d1")
            # form.save()
            print("d2")
            qs.save()
            print("d3")
            return redirect("Essential_view")
        else:
            return render(request, self.template_name,{"form":form})

class viewEssential(TemplateView):
    model_name=Essential
    template_name = "Budgetentry/viewEssential.html"
    # def get_queryset(self):
    #     return self.model_name.objects.all()
    def get(self, request, *args, **kwargs):
        qs = Essential.objects.filter(Username=request.session["Username"])
        context={}
        context["viewessential"]=qs
        return render(request,self.template_name,context)

class updateEssential(UpdateView):
    model=Essential
    fields = ['Category',]
    success_url = '/Viewessential'
    # success_url = reverse_lazy('getRes')
    #context_object_name = "form"
    template_name = 'Budgetentry/createEssential.html'
class deleteEssential(DeleteView):
    model = Essential
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    fields = ['Category']
    # template_name_suffix = "_del"
    success_url = '/Viewessential'


class createEntry(TemplateView):
    # Username=None
    # def get(self):
    #     print("ggg")

    # global x
    # print(x)
    # User1=request.session['Username']
    form_class=Addentryform
    model_name=Entry
    template_name = "Budgetentry/createEntry.html"

    # def form_valid(self, form):
    #     Entry = form.save(commit=False)
    #
    #     Entry.Username=Users.objects.get(Username=self.request.Username)  # use your own profile here
    #     Entry.save()
    #     print("aa")
    #     return HttpResponseRedirect(self.get_success_url())
    # def get_form(self, form_class):
    #     u = request.session['Username']
    #     print("uuuu:",u)
    #     if form_class:
    #         form_class = self.get_form_class()
    #         print("ssss:",form_class)
    #     return form_class(user=self.request.user, **self.get_form_kwargs())

    # def get_form_kwargs(self):
    #     u=request.session["Username"]
    #     kwargs = super(Addentryform, self).get_form_kwargs()
    #     kwargs['host'] = u
    #     return kwargs
    def get(self,request,*args,**kwargs):
        u = request.session['Username']
    #     return redirect("view_paymode")
        context={}


        context["form"]=self.form_class(u)

        # form_class=Addentryform(u)
        print("ffffff")
        # return self.form_class(user=self.request.user, **self.get_form_kwargs())
        return render(request,self.template_name(),{"form":self.form_class})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)

        print("0000")
        if form.is_valid():
            print("11111")


            Username = request.session["Username"]
            Paymode = form.cleaned_data["Paymode"]
            Category = form.cleaned_data["Category"]
            Amount=form.cleaned_data["Amount"]
            Dfield = form.cleaned_data["Dfield"]

            print("sess:",request.session["Username"])
            print("cat:",Category)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs =Entry.objects.create(Username=Username,Paymode=Paymode,\
                                     Category=Category,Amount=Amount,\
                                     Dfield=Dfield)
            print("d1")
            # form.save()
            print("d2")
            qs.save()
            print("d3")
            return redirect("Entry_view")
        else:
            return render(request, self.template_name,{"form":form})

class viewEntry(TemplateView):
    model_name=Entry
    template_name = "Budgetentry/viewEntry.html"
    # def get_queryset(self):
    #     return self.model_name.objects.all()
    def get(self, request, *args, **kwargs):
        qs = Entry.objects.filter(Username=request.session["Username"])
        context={}
        context["viewentry"]=qs
        return render(request,self.template_name,context)

class updateEntry(UpdateView):
    model=Entry
    fields = ['Username','Paymode','Category','Amount','Dfield',]
    success_url = '/Viewentry'
    # success_url = reverse_lazy('getRes')
    #context_object_name = "form"
    template_name = 'Budgetentry/createEntry.html'
class deleteEntry(DeleteView):
    model = Entry
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    fields = ['Username','Paymode','Category','Amount','Dfield',]
    # template_name_suffix = "_del"
    success_url = '/Viewentry'


class createCategorywise(TemplateView):
    form_class=Addcategorywiseform
    model_name=Entry
    template_name = "Budgetentry/createCategorywise.html"
    template_name1 = "Budgetentry/viewCategorywise.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("0000")
        if form.is_valid():
            print("11111")
            Username = request.session["Username"]
            Category = form.cleaned_data["Category"]
            print("sess:",request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs =Entry.objects.filter(Username=Username,Category__Category=Category).values('Category__Category') \
                    .annotate(Total=Sum('Amount'))
            print("d1")
            # xx=[]
            # for i in qs:
            #     print(i.get("Category__Category"))
            # x=[i.get("Category__Category") for i in qs]
            # print(x)
            # y = [i.get("Total") for i in qs]
            # print(y)
            #
            # # print(qs.Category__Category)
            #
            # x_data = [i.get("Category__Category") for i in qs]
            # print(x_data)
            # y_data = [i.get("Total") for i in qs]
            # plot_div = plot([Scatter(x=x_data, y=y_data,
            #                          mode='lines', name='test',
            #                          opacity=0.8, marker_color='green')],
            #                 output_type='div')
            context = {}
            context["viewcatwise"] = qs
            return render(request, self.template_name1, context)

            # form.save()
            print("d2")
            # qs.save()
            print("d3")
            # return redirect("Categorywise_view")
        else:
            return render(request, self.template_name,{"form":form})

class createDatewise(TemplateView):
    form_class=Adddatewiseform
    model_name=Entry
    template_name = "Budgetentry/createDatewise.html"
    template_name1 = "Budgetentry/viewDatewise.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("0000")
        if form.is_valid():
            print("11111")
            Username = request.session["Username"]
            Category = form.cleaned_data["Category"]
            Startdate = form.cleaned_data["Startdate"]
            Enddate = form.cleaned_data["Enddate"]
            print("sess:",request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs =Entry.objects.filter(Username=Username, \
                    Dfield__range=[Startdate,Enddate],\
                                        # Dfield__lte=Enddate, \
                    Category__Category=Category)\
                    .aggregate(Total=Sum('Amount'))
            # print(qs.Total)
            # qs =Entry.objects.filter(Q(Username=Username)& \
            #                          Q(Dfield__gte=Startdate)&\
            #                          Q(Dfield__lte=Enddate)&\
            #                          Q(Category__Category=Category)).\
            #     aggregate(Sum('Amount')).get('Amount__sum')
            print("d1")
            context = {}
            context["vdw"] = qs
            context["un"]=Username
            context["sd"]=Startdate
            context["ed"]=Enddate
            context["ct"]=Category
            return render(request, self.template_name1, context)

            # form.save()
            print("d2")
            # qs.save()
            print("d3")
            # return redirect("Categorywise_view")
        else:
            return render(request, self.template_name,{"form":form})
# class viewCategorywise(TemplateView):
#     model_name=Entry
#     template_name = "Budgetentry/viewCategorywise.html"
#     def get_queryset(self):
#         return self.model_name.objects.filter(Username=Username).values('category__category')\
#             .annotate(tot=Sum('amount'))
#     def get(self, request, *args, **kwargs):
#         context={}
#         context["viewaccount"]=self.get_queryset()
#         return render(request,self.template_name,context)

def createOverallcategory(request):

            Username = request.session["Username"]
            # Category = form.cleaned_data["Category"]
            print("sess:",request.session["Username"])
            # print("pay:",Paymode)
            # Username1 = request.session.Username
            # Username=form.cleaned_data["Username"]
            qs =Entry.objects.filter(Username=Username).values('Category__Category') \
                    .annotate(Total=Sum('Amount'))
            print("d1")
            # xx=[]
            # for i in qs:
            #     print(i.get("Category__Category"))
            # x=[i.get("Category__Category") for i in qs]
            # print(x)
            # y = [i.get("Total") for i in qs]
            # print(y)

            # print(qs.Category__Category)

            x_data = [i.get("Category__Category") for i in qs]
            print(x_data)
            y_data = [i.get("Total") for i in qs]
            fig = go.Figure(data=[go.Pie(labels=x_data, values=y_data)])
            fig.show()
            # fig = go.Figure(data=[go.Bar(
            #     x=x_data, y=y_data,
            #     text=y_data,
            #     textposition='auto',
            # )])
            #
            # fig.show()
            plot_div = plot(fig, output_type='div')
            # plot_div = plot([Scatter(x=x_data, y=y_data,
            #                          mode='lines', name='test',
            #                          opacity=0.8, marker_color='green')],
            #                 output_type='div',include_plotlyjs=False)
            context = {}
            context["viewoverall"] = qs
            return render(request, 'Budgetentry/viewOverallcategory.html', context={'plot_div': plot_div,"viewoverall":qs})

            # form.save()
            print("d2")
            # qs.save()
            print("d3")
            # return redirect("Categorywise_view")
        # else:
        #     return render(request, self.template_name,{"form":form})

# class viewPaymode(CreateView):
#     template_name = 'Budgetentry/paymode.html'
#     model = Entry
#     form_class = Addentryform
#     Username = None
#
#     # Set the success url to be the current url so the same page is loaded after submission.
#     def get_success_url(self):
#         return self.request.path
#
#     # Set the pricelist form field from the pricelist pk
#     def get_initial(self):
#         self.Username =
#
#         return {
#             'Username':self.Username,
#         }
#
#     #Add pricelist data to the context
#     def get_context_data(self, *args, **kwargs):
#         context = super(viewPaymode, self).get_context_data(*args, **kwargs)
#         context['Username'] = self.Username
#         return context