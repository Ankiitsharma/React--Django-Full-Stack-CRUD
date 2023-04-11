from rest_framework import serializers
from .models import StudentModal

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentModal
        fields = ['id', 'stuname', 'email']