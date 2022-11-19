# Dpt_Back

    pip install django
    pip install djangorestframework
    pip install django-extensions
    pip install pyJWT
  
  
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
   
