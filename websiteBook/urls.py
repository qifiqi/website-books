"""websiteBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from websiteBook import settings
from notebooks.views import home
from creative_page import views
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import re_path  # 因为需要用到正则匹配所以导入它

urlpatterns = [
                  # 后台管理
                  path('admin/', admin.site.urls),

                  # 首页
                  path("", home.Home.as_view(), name="home"),
                  # 表白
                  path("xiaofu_xiaochen", views.xiaofu_xiaochen, name="xiaofu_xiaochen"),

                  # 笔记页
                  path('notebooks/', include(("notebooks.urls", "notebooks"), namespace="notebook")),
                  # 创意页面
                  path('creative_page/', include(("creative_page.urls", "creative_page"), namespace="creative_pages")),
                  # 静态文件加载问题
                  re_path('^static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}),  # 用于处理static里的文件

                  # re_path('^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),  # 用于处理上传的文件
              ]

"""
                              _ooOoo_
                             o8888888o
                             88" . "88
                             (| -_- |)
                             O\  =  /O
                          ____/`---'\____
                        .'  \\|     |//  `.
                       /  \\|||  :  |||//  \
                      /  _||||| -:- |||||-  \
                      |   | \\\  -  /// |   |
                      | \_|  ''\---/''  |   |
                      \  .-\__  `-`  ___/-. /
                    ___`. .'  /--.--\  `. . __
                 ."" '<  `.___\_<|>_/___.'  >'"".
                | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                \  \ `-.   \_ __\ /__ _/   .-` /  /
           ======`-.____`-.___\_____/___.-`____.-'======
                              `=---='
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                      佛祖保佑        永无BUG
             佛曰:
                    写字楼里写字间，写字间里程序员；
                    程序人员写程序，又拿程序换酒钱。
                    酒醒只在网上坐，酒醉还来网下眠；
                    酒醉酒醒日复日，网上网下年复年。
                    但愿老死电脑间，不愿鞠躬老板前；
                    奔驰宝马贵者趣，公交自行程序员。
                    别人笑我忒疯癫，我笑自己命太贱；
                    不见满街漂亮妹，哪个归得程序员？
"""
