# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
from users.models import User

def welcome(request):
    return render_to_response('login.html')

def login(request):
    userName = request.POST['userName']
    password = request.POST['password']
    error = {}
    if userName.strip() == "":
        error['NAME_ERR'] = 'User name is required.'
    if password.strip() == "":
        error['PASS_ERR'] = 'Password is required.'
    if error:
        return render(request, 'login.html', {'error_msg': error})

    try:
        user = User.objects.get(user_name = userName, password = password)
    except Exception as e:
        return render(request, 'login.html', {'error': 'Username or password mistake.'})
    else:
        return render(request, 'question_list.html', {'user': user})
