from datetime import date

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from playground.models import Cust, Credit


# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if username != "" and password != "":
        if user is not None:
            auth.login(request, user)
            return JsonResponse({'status': 200, 'message': 'login success!'})
        else:
            return JsonResponse({'status': 10002, 'message': 'username or password error'})
    else:
        return JsonResponse({'status': 10003, 'message': 'paramater error'})



def signin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    is_superuser = request.POST.get('is_superuser', '')
    is_staff = request.POST.get('is_staff', '')

    if username == "" or password == "" or is_staff == "" or is_superuser == "":
        return JsonResponse({'status': 10003, 'message': 'paramater error'})

    if not User.objects.filter(username=username):
        now = str(date.today())
        User.objects.create_user(username=username, password=password, is_superuser=is_superuser, is_active=1, is_staff=is_staff, date_joined=now)
        return JsonResponse({'status': 200, 'message': 'add user success'})
    else:
        return JsonResponse({'status': 10005, 'message': 'user has already exists'})

def get_credit(request):
    cust_id = request.POST.get('cust_id', '')
    if cust_id == '':
        return JsonResponse({'status': 10003, 'message': 'paramater error'})
    if not Cust.objects.filter(id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'cust does not exist'})
    if not Credit.objects.filter(cust_id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'credit does not exist'})
    else:
        cust_id = cust_id
        credit_value = Credit.objects.get(cust_id=cust_id).credit_value
        data = {'cust_id': cust_id, 'credit_value': credit_value }
        return JsonResponse({'status': 200, 'data': data})





def add_credit(request):
    cust_id = request.POST.get('cust_id', '')
    credit_value = request.POST.get('credit_value', '')

    if cust_id == '' or credit_value == '':
        return JsonResponse({'status': 10003, 'message': 'paramater error'})

    if not Cust.objects.filter(id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'cust does not exist'})
    elif Credit.objects.filter(cust_id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'credit has already exists'})
    else:
        now = str(date.today())
        Credit.objects.create(cust_id=cust_id, create_date=now, modify_date=now, credit_value=credit_value)
    return JsonResponse({'status': 200, 'message': 'add credit success'})


def delete_credit(request):
    cust_id = request.POST.get('cust_id', '')
    if cust_id == '':
        return JsonResponse({'status': 10003, 'message': 'paramater error'})
    if not Cust.objects.filter(id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'cust does not exist'})
    if not Credit.objects.filter(cust_id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'credit does not exist'})
    else:
        Credit.objects.filter(cust_id=cust_id).delete()
    return JsonResponse({'status': 200, 'message': 'delete credit success'})


def alter_credit(request):
    cust_id = request.POST.get('cust_id', '')
    credit_value = request.POST.get('credit_value', '')

    if cust_id == '' or credit_value == '':
        return JsonResponse({'status': 10003, 'message': 'paramater error'})
    if not Cust.objects.filter(id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'cust does not exist'})
    if not Credit.objects.filter(cust_id=cust_id):
        return JsonResponse({'status': 10006, 'message': 'credit does not exist'})
    else:
        now = str(date.today())
        Credit.objects.filter(cust_id=cust_id).update(credit_value=credit_value,modify_date=now)
    return JsonResponse({'status': 200, 'message': 'alter credit success'})









