from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# Create your views here.
class Home(View):

    @method_decorator(cache_page(24 * 60 * 60))
    def get(self, requests):
        return render(requests, "home.html", locals())

    def post(self, requests):
        pass
