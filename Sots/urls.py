"""Sots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import administrators.adminuser.adminuser as ad
import administrators.models as admo
import administrators.user.user as us
import administrators.job.job as job
import administrators.company.company as com
from analysis.views import access, into_mysql, write_djob, index, job_list
import administrators.website.website as web
import analysis.personalCenter as pc

import administrators.test.test as te

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 后台
    url(r'admin/login$', ad.land, name='login'),  # 管理员登陆界面，
    url(r'admin/checks$', ad.checks, name='checks'),# 后台校验用户名和密码
    url(r'admin/main$', ad.show_main, name='main'),# 主界面
    url(r'admin/welcome$', ad.welcome, name='welcome'),#  欢迎分界面
    url(r'admin/repassword$', ad.repassword, name='repassword'),# 修改管理员密码
    url(r'admin/adminUpdate$', ad.update, name='adminUpdate'),# 完成修改
    url(r'admin/login$', ad.exit, name='exit'),



    # 用户
    url(r'admin/userShow', us.show, name='userShow'),# 用户展示
    url(r'admin/userDel*', us.delete, name='userDel'),# 用户删除
    url(r'admin/userAdd', us.add, name='userAdd'),# 跳转到添加用户界面
    url(r'admin/userSave', us.save, name='userSave'),# 用户存储
    url(r'admin/userEdit', us.edit, name='userEdit'),# 跳转到编辑用户界面
    url(r'admin/userUpdate', us.update, name='userUpdate'),# 用户更新

    # 岗位
    url(r'admin/jobShow', job.show, name='jobShow'),# 岗位展示
    url(r'admin/jobDel', job.delete, name='jobDel'),# 岗位删除
    url(r'admin/jobAdd', job.add, name='jobAdd'),# 跳转到添加岗位界面
    url(r'admin/jobSave', job.save, name='jobSave'),# 岗位存储
    url(r'admin/jobEdit', job.edit, name='jobEdit'),# 跳转到编辑岗位界面
    url(r'admin/jobUpdate', job.update, name='jobUpdate'),# 岗位更新

    # 网站
    url(r'admin/websiteShow', web.show, name='websiteShow'),  # 网站展示
    url(r'admin/websiteDel', web.delete, name='websiteDel'),  # 网站删除
    url(r'admin/websiteAdd', web.add, name='websiteAdd'), # 跳转到添加网站界面
    url(r'admin/websiteSave', web.save, name='websiteSave'),  # 网站存储
    url(r'admin/websiteEdit', web.edit, name='websiteEdit'),# 跳转到编辑岗位界面
    url(r'admin/websiteUpdate', web.update, name='websiteUpdate'),# 岗位更新

    # 公司
    url(r'admin/companyShow', com.show, name='companyShow'),  # 公司展示
    url(r'admin/companyDel', com.delete, name='companyDel'),  # 公司删除

    # 前台
    url(r'^$', index, name='index'), # 前台首页
    url(r'api/information', job_list),# 搜索跳转显示结果

    # 前台首页
    #url(r'sots/carouselData', ),# 轮播数据
    # 前台个人中心
    url(r'sots/registered', pc.registered),# 前台注册
    url(r'sots/logIn', pc.login),# 前台登录
    url(r'sots/postPersonalInformation', pc.postPersonalInformation),# 将用户个人信息提交到后台
    url(r'sots/getPersonalInformation', pc.getPersonalInformation),# 前台获得个人信息



    # 测试
    url(r'access', access, name='access'),
    url(r'into_mysql', into_mysql,name='intomysql'),
    url(r'write_djob', write_djob, name='writedjob'),

    # 随机生成求职者的测试数据，存入数据库
    url(r'admin/testShow', te.show, name='testShow'),# 展示页面
    url(r'admin/testRandom',te.rando, name='testRandom'),# 进入后端去生成
    url(r'admin/infoSave',te.save,name='infoSave'),# 存储生成


]
