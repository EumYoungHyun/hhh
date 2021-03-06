from . import models
from rest_framework import serializers


class DiningStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiningStore
        fields = "__all__"


class DiningReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiningReview  # 모델 설정
        fields = "__all__"  # 필드 설정

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location  # 모델 설정
        fields = "__all__"  # 필드 설정

