from django.shortcuts import render, redirect
from .models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods, User
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
import time, random, os
from project import settings
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
def market(request, gid, cid, sortid):
    # 左侧导航
    leftSlider = FoodTypes.objects.all()
    # 顶端分类
    productList = Goods.objects.filter(categoryid=gid)
    if cid != '0':
        productList = productList.filter(childcid=cid)
    # 分类
    if sortid == '1':
        productList = productList.order_by('-productnum')
    elif sortid == '2':
        productList = productList.order_by('price')
    elif sortid == '3':
        productList = productList.order_by('-price')

    # 获取分类名称
    childtype = FoodTypes.objects.get(typeid=gid).childtypenames
    strList = childtype.split('#')
    childList = []
    for str in strList:
        myStr = str.split(':')
        childList.append({'childId': myStr[1], 'childName': myStr[0]})

    return render(request, 'shaxf/market/market.html', {'title': '闪购超市', 'leftSlider': leftSlider,
                                                        'productList': productList, 'childList': childList,
                                                        'cid': cid, 'gid': gid})

# 购物车
def cart(request):
    return render(request, 'shaxf/carts/carts.html', {'title': '购物车'})

# 我的
def mine(request):
    key = request.COOKIES.get('name')
    userName = request.session.get(key, '未登录')
    token = request.COOKIES.get('token')
    try:
        userImg = User.objects.get(userToken=token).userImg
        print(userImg)
        return render(request, 'shaxf/mine/mine.html', {'title': '我的', 'userName': userName, 'userImg': userImg})
    except User.DoesNotExist as e:
        return render(request, 'shaxf/mine/mine.html', {'title': '我的', 'userName': userName})
# 登陆
def login(request):

    # 判断请求类型
    if request.method == 'GET':
        # 之前请求的页面, 在收到GET请求时保存其发起网址，存储到session 用于后期重定向
        reAddr = request.META['HTTP_REFERER']
        request.session['reAddr'] = reAddr
        return render(request, 'shaxf/mine/login.html')

    # 获取输入的用户名和密码
    loginUser = request.POST.get('username')
    loginPassWd = request.POST.get('passwd')

    # 判断表中是否存在该用户
    try:
        user = User.objects.get(userAccount=loginUser)
    except User.DoesNotExist as e:
        return redirect('/login/')

    # 既存在该用户， 密码又相同，那么就登陆成功，
    if loginPassWd == user.userPasswd:
        # 获取最初发起请求网址
        addr = request.session.get('reAddr')
        # 并且重新生成一个token值 也保存到数据库也保存到cookies 用户后期判断用户登录状态
        token = str(time.time())[6:] + user.userName
        user.userToken = token
        user.save()

        res = redirect(addr)
        request.session['name'] = user.userName
        res.set_cookie('name', 'name')
        res.set_cookie('token', token)
        return res

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'shaxf/mine/register.html')
    # 账号
    userAccount = request.POST.get('userAccount')
    try:
        # 如果用户已经存在则返回1
        dbUser = User.objects.get(userAccount=userAccount)
        return JsonResponse({'data': 1})

    except User.DoesNotExist as e:
        # 密码
        userPass = request.POST.get('userPass')
        userPasswd = request.POST.get('userPasswd')
        # 用户名
        userName = request.POST.get('userName')
        # 手机号
        userPhone = request.POST.get('userPhone')
        # 用户地址
        userAdderss = request.POST.get('userAdderss')
        # 处理用户上传的照片
        imgObj = request.FILES.get('userImg')
        filePath = os.path.join(settings.MEDIA_ROOT[0], imgObj.name)
        with open(filePath, 'wb') as file:
            for c in imgObj.chunks():
                file.write(c)

        # 在数据库中存储用户头像地址
        path = filePath.split("\\")[-3:]
        myPath = ''
        for i in path:
            myPath += '/' + i
        userImg = myPath

        # 随机生成token
        token = str(time.time())[6:] + str(userAccount)

        # 在数据库中创建用户
        user = User.createuser(userAccount, userPasswd, userName, userPhone, userAdderss, userImg, 1, token)
        user.save()

        # 令当前注册账号为登陆状态
        request.session['name'] = userAccount
        res = redirect('/mine/')
        res.set_cookie('name', 'name')
        res.set_cookie('token', token)

        return res

# 退出
def quit(request):
    logout(request)
    res = redirect('/mine/')
    res.delete_cookie('token')
    return res
