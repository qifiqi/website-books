from django.shortcuts import render


# Create your views here.
def jtcsy(requests):
    return render(requests, "creative_page/今天吃啥呀？.html")


def xiaofu_xiaochen(requests):
    return render(requests, "creative_page/表白.html")
