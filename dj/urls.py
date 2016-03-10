"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from route import views as route_views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # 以上路由为自定义路由，为满足特殊的需要

    # 此路由为自动发现路由，如无特殊需要,参照 route/views.py 中的说明使用即可
    # 注意：此路由必须放置在最下方，以防止覆盖自定义路由的实现
    url(r'^(.*)/(.*)', route_views.route),
    url(r'^(.*)/(.*)/(.*)', route_views.route),
]