#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : account.py
# @Author : Hython
# @Date   : 公元 2021/01/23 1:21
from django.shortcuts import render, HttpResponse


def user_login(request):
    return HttpResponse("登陆页面")
