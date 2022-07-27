from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *


def sign_in(request):
    if request.method == "POST":
        pname = request.POST['Username']
        pcode = request.POST['Password']
        record = signin.objects.filter(username=pname, password=pcode)
        print(record)
        if record:
            return HttpResponseRedirect('/search/')
    return render(request, 'signin.html', {})


def log_in(request):
    if request.method == "POST":
        pname = request.POST['Username']
        pcode = request.POST['Password']
        record = signin.objects.filter(username=pname, password=pcode)
        print(record)
        if record:
            return HttpResponseRedirect('/search/')
    return render(request, 'signin.html', {})


def registerview(request):
    if request.method == 'POST':
        wfname = request.POST['FirstName']
        wlname = request.POST['LastName']
        wpassword = request.POST['Password']
        wcpassword = request.POST['ConfirmPassword']
        wemail = request.POST['EmailID']
        wphno = request.POST['Phone_Number']
        wplace = request.POST['Address']
        wgender = request.POST['Gender']
        wbg = request.POST['Blood_Group']
        record = register.objects.create(firstname=wfname, lastname=wlname, password=wpassword,
                                         confirm_password=wcpassword, email_id=wemail, ph_no=wphno, place=wplace,
                                         gender=wgender, blood_group=wbg)
        print(record)
        return HttpResponseRedirect('/datas/')
    return render(request, 'blood_reg.html', {})


def blood_search(request):
    if request.method == 'POST':
        bloodtype = request.POST['blood type']
        record = blooddata.objects.filter(blood_group=bloodtype)
        print(record)
        return render(request, 'blood_stock.html', {'datas': record})
    return render(request, 'blood_search.html', {})


def blood_records(request):
    if request.method == "POST":
        f1 = blooddataform(request.POST)
        if f1.is_valid():
            f1.save()
            return HttpResponseRedirect('/search/')
    f2 = blooddataform
    return render(request, 'blood_data.html', {'form': f2})


def newpage(request):
    if request.method == "POST":
        tname = request.POST['Username']
        tcode = request.POST['Password']
        record = signin.objects.create(username=tname, password=tcode)
        print(record)
        if record:
            return HttpResponseRedirect('/search/')
    return render(request, 'newpage.html', {})


def homepage(request):
    return render(request, 'homepage.html', {})

