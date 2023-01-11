from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 60)
def jtcsy(requests):
    return render(requests, "creative_page/今天吃啥呀？.html")


@cache_page(60 * 60)
def xiaofu_xiaochen(requests):
    return render(requests, "creative_page/表白.html")
