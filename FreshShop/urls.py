"""FreshShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

import xadmin
from FreshShop.settings import MEDIA_ROOT
from django.views.static import serve
#引入文档
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from goods.views import GoodsListViewSet, CategoryViewSet
router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

# xadmin.autodiscover()
#
# from xadmin.plugins import xversion
# xversion.register_models()



# goods_list= GoodsListViewSet.as_view({
# #     'get': 'list',
# #     # 'post': 'create'
# # })

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 配置drf登录的api，调试api用到
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 商品列表页
    # url(r'goods/$', GoodsListViewSet.as_view(), name="goods-lits"),

    # 某一条数据详情页
    # url(r'^(?P<pk>[0-9]+)/$', HouseKeeperDiaryView.as_view(), name="diary_detail")

    url(r'^', include(router.urls)),
    # 文档的配置
    url(r'docs/', include_docs_urls(title="千寻生鲜")),

# drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),


]
