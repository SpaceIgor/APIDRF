from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Direction, Doctor


class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direction
        fields = "__all__"


class DoctorSerializer(serializers.ModelSerializer):
    direction = serializers.StringRelatedField(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name_doctor', 'slug', 'direction', 'date_of_birth', 'experience', 'description', ]