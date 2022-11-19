from django.db import models
from authentiacation.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.question}'

class NewAnswer(models.Model):
    # 1번 question
    question1 = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name='question1')
    answer1 = models.CharField(max_length=20)
    option1_1 = models.CharField(max_length=20)
    option1_2 = models.CharField(max_length=20, null=True, blank=True)
    option1_3 = models.CharField(max_length=20, null=True, blank=True)
    option1_4 = models.CharField(max_length=20, null=True, blank=True)

    # 2번 question
    question2 = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name='question2')
    answer2 = models.CharField(max_length=20)
    option2_1 = models.CharField(max_length=20)
    option2_2 = models.CharField(max_length=20, null=True, blank=True)
    option2_3 = models.CharField(max_length=20, null=True, blank=True)
    option2_4 = models.CharField(max_length=20, null=True, blank=True)

    # 3번 question
    question3 = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name='question3')
    answer3 = models.CharField(max_length=20)
    option3_1 = models.CharField(max_length=20)
    option3_2 = models.CharField(max_length=20, null=True, blank=True)
    option3_3 = models.CharField(max_length=20, null=True, blank=True)
    option3_4 = models.CharField(max_length=20, null=True, blank=True)

    # 4번 question
    question4 = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name='question4')
    answer4 = models.CharField(max_length=20)
    option4_1 = models.CharField(max_length=20)
    option4_2 = models.CharField(max_length=20, null=True, blank=True)
    option4_3 = models.CharField(max_length=20, null=True, blank=True)
    option4_4 = models.CharField(max_length=20, null=True, blank=True)

    # 5번 question
    question5 = models.ForeignKey(Question, on_delete=models.CASCADE,
        related_name='question5')
    answer5 = models.CharField(max_length=20)
    option5_1 = models.CharField(max_length=20)
    option5_2 = models.CharField(max_length=20, null=True, blank=True)
    option5_3 = models.CharField(max_length=20, null=True, blank=True)
    option5_4 = models.CharField(max_length=20, null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = []
    options = []
    id = models.AutoField(primary_key=True)

    def create(self, validated_data):
        self.answers.append(self.answer1)
        self.answers.append(self.answer2)
        self.answers.append(self.answer3)
        self.answers.append(self.answer4)
        self.answers.append(self.answer5)

        self.options.append([self.answer1,self.option1_1,self.option1_2,self.option1_3,self.option1_4])
        self.options.append([self.answer2,self.option2_1,self.option2_2,self.option2_3,self.option2_4])
        self.options.append([self.answer3,self.option3_1,self.option3_2,self.option3_3,self.option3_4])
        self.options.append([self.answer4,self.option4_1,self.option4_2,self.option4_3,self.option4_4])
        self.options.append([self.answer5,self.option5_1,self.option5_2,self.option5_3,self.option5_4])
        self.save()


class Cookie(models.Model):
    id = models.AutoField(primary_key=True)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f'cookie{self.id}'

class Maker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cookie = models.ForeignKey(Cookie, on_delete=models.CASCADE)

class Guest(models.Model):
    nickname = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)
    answer5 = models.CharField(max_length=20)
    answers = []

    score = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['score', 'nickname']

# class CookieList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     nickname = models.CharField(max_length=30)
#     score = models.IntegerField(default=0, null=True, blank=True)

#     def __str__(self):
#         return f"{self.nickname} : {self.score}"