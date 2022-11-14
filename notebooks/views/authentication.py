# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/11/1419:55
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : authentication.py
__author__ = 'Small Fu'

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse


class Login(View):
    def get(self, requests):
        return render(requests, "notebooks/authentication/login.html", locals())

    def post(self, requests):
        print(requests)
        back_dict = {"code":200}
        back_dict["code"] = 2001
        back_dict["msg"] = "失败"
        return JsonResponse(back_dict)


class Register(View):
    def get(self, requests):
        return HttpResponse("Register get")

    def post(self, requests):
        return HttpResponse("Register post")

