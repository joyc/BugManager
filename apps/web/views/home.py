#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : home.py
# @Author : Hython
# @Date   : 公元 2021/01/23 1:21
from django.shortcuts import render


def index(request):
    """top page"""
    return render(request, 'home.html')
