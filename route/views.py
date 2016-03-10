from django.shortcuts import render

# 需要实现自动路由必须遵循以下规则
# 1. 所有 app-name 和 fun-name 必须为全小写，单词间隔符统一使用下划线 '_'
# 2. 所有方法必须定义在对应的 app 的 views.py 文件中
# 3. 新建 app 必须在此文件中显式引入资源，其格式如下
#    from app-name import views as app-name_views

from route import views as route_views
from home import views as home_views

# Create your views here.

def route(request, a, b):
    exc = "%s_views.%s(request)" %(a.lower(),b.lower())
    return eval(exc)