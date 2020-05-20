"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Userdetail import views
from Budgetentry import views
from Budgetentry.views import *
urlpatterns = [
    # path('Addaccount', views.createAccount.as_view(),name="Account_create"),
    path('Addaccount', lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
            (views.createAccount.as_view()(request)),name="Account_create"),
    path('Viewaccount',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
        (views.viewAccount.as_view()(request)), name="Account_view"),
    path('AddEssential',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
        (views.createEssential.as_view()(request)), name="Essential_create"),
    path('Viewessential',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
        (views.viewEssential.as_view()(request)), name="Essential_view"),
    path('Addentry',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
            (views.createEntry.as_view()(request)), name="Entry_create"),
    path('Viewentry',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
            (views.viewEntry.as_view()(request)), name="Entry_view"),
    path('Addcategorywise',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
        (views.createCategorywise.as_view()(request)), name="Categorywise_create"),
    path('Adddatewise',lambda request:redirect('User_login') \
        if ('Username' not in request.session) else \
        (views.createDatewise.as_view()(request)), name="Datewise_create"),
    path('AddOverallcategory',lambda request:redirect('User_login') \
            if ('Username' not in request.session) else \
            (createOverallcategory(request)), name="Overallcategory_create"),
    path('Editaccount/<int:pk>', views.updateAccount.as_view(), name="Account_edit"),
    path('Deleteaccount/<int:pk>', views.deleteAccount.as_view(), name="Account_delete"),
    path('Editessential/<int:pk>', views.updateEssential.as_view(), name="Essential_edit"),
    path('Deleteessential/<int:pk>', views.deleteEssential.as_view(), name="Essential_delete"),
    path('Editentry/<int:pk>', views.updateEntry.as_view(), name="Entry_edit"),
    path('Deleteentry/<int:pk>', views.deleteEntry.as_view(), name="Entry_delete"),
    # path('pay', views.viewPaymode.as_view(), name="view_paymode"),



    # path('Home', views.home.as_view(), name="Home"),
    # path("Home",lambda request:render(request,"index.html"),name="User_home"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
