import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class WomenSerializer(serializers.ModelSerializer):
    # cat = CategorySerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"
        # read_only_fields = ['user', ]


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_updated = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_updated = validated_data.get('time_updated', instance.time_updated)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance

# def encode():
#     data = {"title": 'Sher', 'content': 'Dadakhanov'}
#     data_sr = WomenSerializer(data)
#     json = JSONRenderer().render(data_sr.data)
#     print(json)
#
#
# def decode():
#     json = io.BytesIO(b'{"title":"Sher","content":"Dadakhanov"}')
#     data_sr = JSONParser().parse(json)
#     serializer = WomenSerializer(data=data_sr)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)
