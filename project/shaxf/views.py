from django.shortcuts import render
from .models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods

# Create your views here.
# 首页
def home(request):
    # 轮播图
    imgList = Wheel.objects.all()
    # 导航
    navList = Nav.objects.all()
    # 轮播菜单
    menuNavList = Mustbuy.objects.all()
    # 商品
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1: 3]
    shop3 = shopList[3: 7]
    shop4 = shopList[7: 11]
    # 商品分模块展示
    mainShowList = MainShow.objects.all()
    return render(request, 'shaxf/home/home.html', {'title': '主页', 'imgList': imgList, 'navList': navList,
                                                    'menuNavList': menuNavList, 'shop1': shop1, 'shop2': shop2,
                                                    'shop3': shop3 ,'shop4': shop4,
                                                    'mainShowList': mainShowList})

# 闪购超市
def market(request, typeid, cid):
    leftSlider = FoodTypes.objects.all()
    productList = Goods.objects.filter(categoryid=typeid)
    if cid != '0':
        productList = productList.filter(childcid=cid)
    childtype = FoodTypes.objects.get(typeid=typeid).childtypenames
    strList = childtype.split('#')
    childList = []
    for str in strList:
        myStr = str.split(':')
        childList.append({'childId': myStr[1], 'childName': myStr[0]})
    return render(request, 'shaxf/market/market.html', {'title': '闪购超市', 'leftSlider': leftSlider,
                                                        'productList': productList, 'childList': childList,
                                                        'cid': cid, 'gid': typeid})

# 购物车
def cart(request):
    return render(request, 'shaxf/carts/carts.html', {'title': '购物车'})

# 我的
def mine(request):
    return render(request, 'shaxf/mine/mine.html', {'title': '我的'})