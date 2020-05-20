from urllib import request

from django.http import *
# from django.contrib.sessions.backends.db import SessionStore
# user = request.session["Username"]

from django.db import models
from datetime import *

# from django.http import request
# from pip._vendor.urllib3.util import request
# from pip._vendor.urllib3 import request
from django.urls import reverse
from pyparsing import unicode

from Userdetail.models import *


# Create your models here.
class Account(models.Model):

    Paymode = models.CharField(max_length=250)
    Username = models.CharField(max_length=200, blank=True, null=True)

    # Username = models.ForeignKey(Users,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Paymode) #+ ':' + str(self.Username)

    class Meta:
    #     constraints = [
    #         models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
    #     ]
        unique_together = ("Paymode", "Username")
    # def __str__(self):
    #     return self.Paymode


class Essential(models.Model):
    Category = models.CharField(max_length=250)
    Username = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.Category
    class Meta:
        unique_together = ("Category", "Username")






class Entry(models.Model):
    # class Type(models.TextChoices):
    #     EXPENSE= 'E', _('Expense')
    #     INCOME = 'I', _('Income')
    # uid=models.ForeignKey(Registration,on_delete=models.CASCADE)
    Username = models.CharField(max_length=200,)
    Paymode = models.ForeignKey(Account, on_delete=models.CASCADE)
    Category = models.ForeignKey(Essential, on_delete=models.CASCADE)
    Amount = models.FloatField()
    # type=models.CharField(max_length=1,choices=Type.choices,
    #                       default=Type.EXPENSE,)
    Dfield = models.DateField(default=date.today)

    # dfield = models.DateField()
    # image = models.ImageField(upload_to='images/')
    def __str__(self):
             return self.Paymode
    # data =None
    # formset = AddEntry(data=data, queryset=Users.objects.filter(Username=request.session['Username']))
    # for form in formset:
    # form.fields['Paymode'].Username = Account.objects.filter(Username=request.session['Username'])
    # def __str__(self):
    #     return '{} - {}'.format(self.Paymode, self.Category)
    #
    # def __unicode__(self):
    #     return unicode(self.Username)
    #
    # def get_absolute_url(self):
    #     return reverse('Entry_detail', kwargs={'pk': str(self.id)})

