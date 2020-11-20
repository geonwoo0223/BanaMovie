from rest_framework import serializers
from .models import Board, BoardComment
from django.contrib.auth import get_user_model


class BoardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class BoardSerializer(serializers.ModelSerializer):
    user = BoardUserSerializer()

    class Meta:
        model = Board
        fields = ('id','user','title','content','board_code','created_at','updated_at')


class BoardCommentSerializer(serializers.ModelSerializer):
    user = BoardUserSerializer()
    board = BoardSerializer()

    class Meta:
        model = BoardComment
        fields = ('id','user','board','content','created_at','updated_at')