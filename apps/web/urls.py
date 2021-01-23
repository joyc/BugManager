#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : urls.py
# @Author : Hython
# @Date   : 公元 2021/01/23 1:26
from django.urls import path
from web.views import home, account

urlpatterns = [
    path('', home.index),
    path('login/', account.user_login),
    path('register/', home.register),

]
