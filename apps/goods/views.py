from django.shortcuts import render


# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import status

from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters

from .models import Goods, GoodsCategory
from .filters import GoodsFilter
from .serializers import GoodsSerializer, CategorySerializer
# Create your views here.

# django-rest=framework

class GoodsPagination(PageNumberPagination):
    page_size = 12 # 表示每页的默认值显示数量
    page_size_query_param = 'page_size' #表示url中每页数量参数
    page_query_param = 'page' #表示url中的页码参数
    max_page_size = 100 #表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃

class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    商品列表页,分页，搜索，过滤，排序
    '''
    # queryset = Goods.objects.all()[:10]
    queryset = Goods.objects.all() #查询结果集
    serializer_class = GoodsSerializer #序列化类
    pagination_class = GoodsPagination #自定义分页会覆盖setting.py全局设置
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['name', 'shop_price']
    filter_class = GoodsFilter
    search_fields = ['name','goods_brief', 'goods_desc']
    ordering_fields = ['sold_num', 'add_time', 'shop_price']

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)
    #     return Response(goods_serializer.data)

    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
    retrieve：
        获取某一个商品分类详情
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer