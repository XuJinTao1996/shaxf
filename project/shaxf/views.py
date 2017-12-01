from django.shortcuts import render
from .models import Wheel

# Create your views here.
# 首页
def home(request):
    imgList = Wheel.objects.all()
    return render(request, 'shaxf/home/home.html', {'title': '首页', 'imgList': imgList})

# 闪购超市
def market(request):
    return render(request, 'shaxf/market/market.html', {'title': '闪购超市'})

# 购物车
def cart(request):
    return render(request, 'shaxf/carts/carts.html', {'title': '购物车'})

# 我的
def mine(request):
    return render(request, 'shaxf/mine/mine.html', {'title': '我的'})