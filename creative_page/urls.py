# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/12/1023:01
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : urls.py
__author__ = 'Small Fu'

from django.urls import path
from creative_page import views

urlpatterns = [
    path("jtcsy", views.jtcsy, name="jtcsy"),
]
