from django.conf.urls  import url, include
from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.home),
    url(r'^home/$', views.home),

    # 闪购超市
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market),

    # 购物车
    url(r'^cart/$', views.cart),

    # 我的
    url(r'^mine/$', views.mine),

    # 登陆
    url(r'^login/$', views.login),

    # 注册
    url(r'^register', views.register),

    # 退出登录
    url(r'^quit/$', views.quit)
]