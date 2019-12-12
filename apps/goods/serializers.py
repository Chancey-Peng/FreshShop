from rest_framework import serializers

from goods.models import Goods, GoodsCategory

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         '''
#         Create and return a new `Snippet` instance, given the validated data
#         :param validated_data:
#         :return:
#         '''
#         return Goods.objects.create(**validated_data)

class CategorySerializer3(serializers.ModelSerializer):
    '''
    商品类别序列化，第三商品类别
    '''
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer2(serializers.ModelSerializer):
    '''
    商品类别序列化， 第二商品类别
    '''
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    '''
    商品类别序列化，第一商品类别
    '''
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"

# class GoodCategorySerializer(serializers.ModelSerializer):
#     '''
#     商品类别序列化
#     '''
#     class Meta:
#         model = Goods
#         fields = "__all__"
