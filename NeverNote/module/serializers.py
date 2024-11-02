from rest_framework import serializers

from module.models import NotesModel, UserModel



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        
    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)


class NotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = '__all__'
        
    def create(self, validated_data):
        return NotesModel.objects.create(**validated_data)