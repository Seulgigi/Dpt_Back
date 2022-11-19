# Dpt_Back

    pip install django
    pip install djangorestframework
    pip install django-extensions
    pip install pyJWT
    pip install djangorestframework
    pip install django-cors-headers
  
  
### USER 회원가입

### 회원가입 http://127.0.0.1:8000/users/register
    {
        "username":"사용자이름",
        "password":"비밀번호 네자리"
    }
### 결과
    {
        "username": "사용자이름",
        "token": "토큰생성"
    }
    
    
### USER 로그인
### 로그인 http://127.0.0.1:8000/users/login
    {
        "username":"사용자",
        "password":"비밀번호 네자리"
    }

### 결과
    {
            "user": {
                "username": "사용자",
                "last_login": "2022-00-00 00:00:00.000000+00:00",
                "token": "토큰"
            }
     }
   
### 퀴즈
### 등록 http://127.0.0.1:8000/quiz/cookie/ - POST
    {
        "user":"user(사용자 token 구현 후 넣어주세요)",
        "cookie":"쿠키"
    }
### 목록 http://127.0.0.1:8000/quiz/cookie/ - GET
    {
        "user":"현재는 user id / user(사용자 token 구현 후 넣어주세요)!",
        "cookie":"쿠키"
    }
### 쿠키 해당 질문 http://127.0.0.1:8000/quiz/cookie/<str:id(cookie.id)>/ - GET
    {
        "id":쿠키 id,
        "questions":[
            질문1,
            질문2,
            질문3,
            질문4,
            질문5
        ]
    }
### ANSWER 등록 http://127.0.0.1:8000/quiz/make/newanswer/<str:user>/ - POST
    {
        "question1": 1,
        "answer1": "1번 정답",
        "option1_1": "1번 오답",
        "option1_2": "1번 오답",
        "option1_3": "1번 오답",
        "option1_4": "1번 오답",
        "question2": 2,
        "answer2": "2번 정답",
        "option2_1": "2번 오답",
        "option2_2": "2번 오답",
        "option2_3": "2번 오답",
        "option2_4": "2번 오답",
        "question3": 3,
        "answer3": "3번 정답",
        "option3_1": "3번 오답",
        "option3_2": "3번 오답",
        "option3_3": "3번 오답",
        "option3_4": "3번 오답",
        "question4": 4,
        "answer4": "4번 정답",
        "option4_1": "4번 오답",
        "option4_2": "4번 오답",
        "option4_3": "4번 오답",
        "option4_4": "4번 오답",
        "question5": 5,
        "answer5": "5번 정답",
        "option5_1": "5번 오답",
        "option5_2": "5번 오답",
        "option5_3": "5번 오답",
        "option5_4": "5번 오답",
        "user": user.id
    }
### ANSWER 등록 http://127.0.0.1:8000/quiz/make/newanswer/<str:user>/ - POST
    {
        "question1": 1,
        "answer1": "1번 정답",
        "option1_1": "1번 오답",
        "option1_2": "1번 오답",
        "option1_3": "1번 오답",
        "option1_4": "1번 오답",
        "question2": 2,
        "answer2": "2번 정답",
        "option2_1": "2번 오답",
        "option2_2": "2번 오답",
        "option2_3": "2번 오답",
        "option2_4": "2번 오답",
        "question3": 3,
        "answer3": "3번 정답",
        "option3_1": "3번 오답",
        "option3_2": "3번 오답",
        "option3_3": "3번 오답",
        "option3_4": "3번 오답",
        "question4": 4,
        "answer4": "4번 정답",
        "option4_1": "4번 오답",
        "option4_2": "4번 오답",
        "option4_3": "4번 오답",
        "option4_4": "4번 오답",
        "question5": 5,
        "answer5": "5번 정답",
        "option5_1": "5번 오답",
        "option5_2": "5번 오답",
        "option5_3": "5번 오답",
        "option5_4": "5번 오답",
        "user": user.id,
        "answers": [
            "1번 정답",
            "2번 정답",
            "3번 정답",
            "4번 정답",
            "5번 정답"
        ],
        "options": [
            [
                "1번 정답",
                "1번 오답",
                "1번 오답",
                "1번 오답",
                "1번 오답"
            ],
            [
                "2번 정답",
                "2번 오답",
                "2번 오답",
                "2번 오답",
                "2번 오답"
            ],
            [
                "3번 정답",
                "3번 오답",
                "3번 오답",
                "3번 오답",
                "3번 오답"
            ],
            [
                "4번 정답",
                "4번 오답",
                "4번 오답",
                "4번 오답",
                "4번 오답"
            ],
            [
                "5번 정답",
                "5번 오답",
                "5번 오답",
                "5번 오답",
                "5번 오답"
            ]
        ]
    }
### GUEST 퀴즈 풀기
### http://127.0.0.1:8000/quiz/<str:user(user.name)>/ - POST
    {
        "nickname": "nickname",
        "user": user(make).id,
        "answer1": "1번 options",
        "answer2": "2번 options",
        "answer3": "3번 options",
        "answer4": "4번 options",
        "answer5": "5번 options"
    }
### http://127.0.0.1:8000/quiz/<str:user(user.name)>/ - GET (list score 순서대로 order)
    {
        "nickname": "nickname",
        "user": user(make).id,
        "answer1": "1번 options",
        "answer2": "2번 options",
        "answer3": "3번 options",
        "answer4": "4번 options",
        "answer5": "5번 options",
        "score":"맞은 개수"
    }