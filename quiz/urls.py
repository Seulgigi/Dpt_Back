from django.urls import path
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('cookie/', CookieChoice.as_view()),
    path('cookie/<str:id>/', QuestionList.as_view()), 
    # path('make/answer/<str:user>/', AnswerCreate.as_view()),
    path('make/answer/<str:user>/', NewAnswerCreate.as_view()),
    path('<str:user>/', GuestCreate.as_view()), 
    # path('cookie/list/<str:name>', CookieList.as_view()),
]