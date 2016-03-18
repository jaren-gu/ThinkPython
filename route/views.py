# 需要实现自动路由必须遵循以下规则
# 1. 所有 app-name ，controller-name ，fun-name 必须为全小写，单词间隔符统一使用下划线 '_'
# 2. 所有 controller 必须定义在对应的 app 的 controllers 文件中
# 3. 所有 function 必须定义在 controllers 下的某个 controller 中

# import importlib

# import home.controllers
# Create your views here.


def reg_route(request, a, b, c):
    # 获取模块
    exec("from %s.controllers import %s" % (a.lower(), b.lower()))
    app = __import__(a.lower())
    # 获取控制器
    controller = getattr(getattr(app, "controllers"), b.lower())
    # 获取方法
    method = getattr(controller, c.lower())
    # 执行并返回结果
    return method(request)


def base_route(request):
    # 获取模块
    exec("from %s.controllers import %s" % (request.GET ['m'].lower(), request.GET ['c'].lower()))
    app = __import__(request.GET ['m'].lower())
    # 获取控制器
    controller = getattr(getattr(app, "controllers"), request.GET ['c'].lower())
    # 获取方法
    method = getattr(controller, request.GET ['a'].lower())
    # 执行并返回结果
    return method(request)
