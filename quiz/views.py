from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.views import View
from django.http import Http404, HttpResponse
from rest_framework import generics, status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
import json

# Create your views here.

# 사용자에게 쿠키 값 넘기기
class CookieChoice(generics.ListCreateAPIView):
    serializer_class = CookieChoiceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Maker.objects.all()

# 쿠키마다 질문 보이기 -> question 값 id-> string 후에 수정
class QuestionList(generics.RetrieveAPIView):
    serializer_class = CookieSerializer
    queryset = Cookie.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

# 답 등록 및 전체 QUESTION 보기
class NewAnswerCreate(generics.ListCreateAPIView):
    serializer_class = NewAnswerSerializer
    permission_classes = [IsAuthenticated]
    queryset = NewAnswer.objects.all()

    def get_answer(self):
        data = NewAnswer.objects.get()
        data = data.filter(user=self.request.user)
        data_dict = {
            'answer':[data.answer1, data.answer2, data.answer3, data.answer4, data.answer5],
            'options':[
                [data.option1_1,data.option1_2,data.option1_3,data.option1_4,data.answer1],
                [data.option2_1,data.option2_2,data.option2_3,data.option2_4,data.answer2],
                [data.option3_1,data.option3_2,data.option3_3,data.option3_4,data.answer3],
                [data.option4_1,data.option4_2,data.option4_3,data.option4_4,data.answer4],
                [data.option5_1,data.option5_2,data.option5_3,data.option5_4,data.answer5]
            ],
            'user': data.user
        }
        data_dict.save()
        return Response(data_dict)

class GuestCreate(generics.ListCreateAPIView):
    serializer_class = GuestSerializer
    permission_classes = []
    queryset = Guest.objects.all().order_by('-score')

    # 사용자 등록 답안만 가져온다
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# class GuestCreate(generics.ListCreateAPIView):
#     serializer_class = GuestSerializer
#     permission_classes = []
#     queryset = Guest.objects.all().order_by('score')

#     # 사용자 등록 답안만 가져온다
#     def get_queryset(self):
#         qs = super().get_queryset()
#         qs = qs.filter(user=self.request.user).order_by('score')
#         return qs


class CookieList(generics.ListCreateAPIView):

    serializer_class = CookieListSerializer
    permission_classes = []
    queryset = Guest.objects.all().order_by('-score')
    
    def get_queryset(self):
         qs = Guest().get_queryset()
         qs = qs.filter(user=self.request.user)
         return qs

