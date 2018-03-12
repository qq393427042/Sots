from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from administrators.models import User as ui
from analysis.models import Carousel as c
import random

def show(request):
    return render(request, 'test/show.html')

def rando(request):
    username = ['12424242@qq.com','24242@qq.com','34242@qq.com','66464242@qq.com']
    password = ['123456','1545845','151516','454561632']
    educationRequire = ['中专','大专','本科','硕士','博士']
    major = ['软件工程', '计算机科学', '网络', '信息管理', '计算机工程']
    school = ['清华大学', '北京大学', '中南大学', '吉首大学', '电子科大']
    jobWantedPlace = ['北京', '上海', '广州', '深圳', '杭州']
    experienceRequire = ['0', '2', '5', '8', '10']
    skill = ['5', '10', '15', '20', '0']

    userInfo = ui(username=username[random.randint(0, 4)], password=password[random.randint(0, 4)],
        nickname=username[random.randint(0, 4)],educationRequire = educationRequire[random.randint(0, 4)],
       major = major[random.randint(0, 4)],school = school[random.randint(0, 4)],
       jobWantedPlace = jobWantedPlace[random.randint(0, 4)],
       experienceRequire = experienceRequire[random.randint(0, 4)],
       skill = skill[random.randint(0, 4)])
    print(userInfo.educationRequire)
    return render(request, 'test/show.html', {'userInfo': userInfo})

def save(request):
    educationRequire = request.POST['educationRequire']
    major = request.POST['major']
    school = request.POST['school']
    jobWantedPlace = request.POST['jobWantedPlace']
    experienceRequire = request.POST['experienceRequire']
    skill = request.POST['skill']
    userInfo = ui(educationRequire=educationRequire, major=major, school=school,
                  jobWantedPlace=jobWantedPlace,experienceRequire=experienceRequire,
                  skill=skill)
    userInfo.save()
    return show(request)