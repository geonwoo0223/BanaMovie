import requests

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Board, BoardComment
from .serializers import BoardSerializer, BoardCommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def board_list_create(request):
    if request.method == 'GET':
        boards = Board.objects.order_by('-pk')
        #print("boards=================", boards)
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    
    else :
        boardItem = request.data
        print("=============", request.user)
        board = Board(
            user = request.user,
            title = boardItem['title'],
            content = boardItem['content'],
            board_code = 1 # 자유게시판일 경우 code는 1, 문의게시판 코드 2, .....
        )
        board.save()
        serializer = BoardSerializer(board)

        return Response(serializer.data)


@api_view(['GET'])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = BoardSerializer(board)
    #print("보드???디테일>??", serializer)
    return Response(serializer.data)