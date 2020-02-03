from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from oneLine.models import WiseSaying, Board
from oneLine.serializers import WiseSayingSerializer, BoardSerializer


class WiseSayingView(viewsets.ModelViewSet):
    serializer_class = WiseSayingSerializer
    queryset = WiseSaying.objects.all()


def get_board(id):
    return Board.objects.get(pk=id)


def post(request):
    title = json.loads(request.body)['title']
    content = json.loads(request.body)['content']
    Board.objects.create(title=title, content=content)


@api_view(['GET'])
def boards(request):
    queryset = Board.objects.all()
    return Response(BoardSerializer(queryset, many=True).data)


@api_view(['GET', 'PATCH', 'DELETE'])
def post_board(request, id):
    if request.method == 'GET':
        return Response(BoardSerializer(get_board(id)).data)

    elif request.method == 'PATCH':
        title = json.loads(request.body)['title']
        content = json.loads(request.body)['content']
        Board.objects.filter(pk=id).update(title=title, content=content)
        return Response('성공적으로 수정함!')

    elif request.method == 'DELETE':
        Board.objects.filter(pk=id).delete()
        return Response('성공적으로 삭제함!')


@api_view(['POST'])
def board(request):
    post(request)
    return Response('성공적으로 포스트를 생성함!')
