from django.shortcuts import render,redirect
from .models import Hiretubers
from django.contrib import messages

def hiretuber(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hiretuber = Hiretubers(firstname=firstname,lastname=lastname,tuber_id=tuber_id,tuber_name=tuber_name,
                                email=email,city=city,state=state,phone=phone,
                                message=message,user_id=user_id)
        hiretuber.save()
        messages.success(request,'Thank you for reaching out!!')
        return redirect('youtubers')
