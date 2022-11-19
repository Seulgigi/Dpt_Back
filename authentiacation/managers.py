from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    # All user
    def create_user(self, username, password=None):
    
        if username is None:
            raise TypeError('Users must have a username.')

        if password is None:
            raise TypeError('Users must have a password.')
    
        user = self.model(
        username = username,
        )

        # django 에서 제공하는 password 설정 함수
        user.set_password(password)
        user.save()
        
        return user

    # admin user
    def create_superuser(self, username, password, **extra_fields):
        
        if password is None:
            raise TypeError('Superuser must have a password.')
        
        # "create_user"함수를 이용해 우선 사용자를 DB에 저장
        user = self.create_user(username, password, **extra_fields)
        # 관리자로 지정
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user