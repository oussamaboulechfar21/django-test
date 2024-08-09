# myapp/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserInfoForm
from .models import UserInfo

def add_user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            # بدلاً من إعادة التوجيه إلى قائمة البيانات، نعرض رسالة شكر
            return render(request, 'thank_you.html', {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
            })
    else:
        form = UserInfoForm()
    return render(request, 'add_list.html', {'form': form})


def user_info_list(request):
    users = UserInfo.objects.all()
    return render(request, 'user_info_list.html', {'users': users})
