from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(View):

    def get(self,requests):
        return render(requests, "home.html", locals())

    def post(self,requests):
        pass