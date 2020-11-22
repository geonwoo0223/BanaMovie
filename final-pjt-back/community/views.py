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
from .serializers import BoardSerializer, BoardUserSerializer, BoardCommentSerializer, BoardCommentUserSerializer


# Create your views here.
@api_view(['GET'])
def board_list(request):
    boards = Board.objects.order_by('-pk')
    serializer = BoardUserSerializer(boards, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def board_create(request):
    boardItem = request.data
    print("=============", request.user)
    board = Board(
        user = request.user,
        title = boardItem['title'],
        content = boardItem['content'],
        board_code = 1 # 자유게시판일 경우 code는 1, 문의게시판 코드 2, .....
    )
    board.save()
    serializer = BoardUserSerializer(board)

    return Response(serializer.data)


@api_view(['GET'])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = BoardUserSerializer(board)
    #print("보드???디테일>??", serializer)
    return Response(serializer.data)
    


@api_view(['DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def board_delete_update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'DELETE' :
        serializer = BoardUserSerializer(board)
        if request.user.is_superuser or board.user == request.user :
            board.delete()
        return Response(True)
    else :
        if board.user == request.user : 
            request.data['user'] = request.user.pk
            serializer = BoardSerializer(board, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            else : 
                print("----update error", serializer.errors)
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request, board_pk):
    comments = BoardComment.objects.order_by('-pk').filter(board_id=board_pk)
    serializer = BoardCommentUserSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    commentItem = request.data
    comment = BoardComment(
        board = board,
        user = request.user,
        content = commentItem['content'],
    )
    comment.save()
    serializer = BoardCommentUserSerializer(comment)
    return Response(serializer.data)