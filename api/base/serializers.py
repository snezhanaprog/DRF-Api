from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class SectionSerializer(ModelSerializer):
    persons_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Section
        fields = '__all__'
    def get_persons_count(self, obj):
        count = obj.person_set.count()
        return count

class PersonSerializer(ModelSerializer):
    section = SectionSerializer()
    class Meta:
        model = Person
        fields = ['name', 'bio', 'section']
