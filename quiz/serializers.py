from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class CookieChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ('user', 'cookie')

    def create(self, validated_data):
        data = Maker.objects.create(**validated_data)
        return data

class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = '__all__'

class NewAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewAnswer
        fields = ('user','answers','options',
                'question1','answer1','option1_1','option1_2','option1_3','option1_4',
                'question2','answer2','option2_1','option2_2','option2_3','option2_4',
                'question3','answer3','option3_1','option3_2','option3_3','option3_4',
                'question4','answer4','option4_1','option4_2','option4_3','option4_4',
                'question5','answer5','option5_1','option5_2','option5_3','option5_4')

        
    def create(self, validated_data):
        data = NewAnswer.objects.create(**validated_data)
        data.answers.append(data.answer1)
        data.answers.append(data.answer2)
        data.answers.append(data.answer3)
        data.answers.append(data.answer4)
        data.answers.append(data.answer5)

        data.options.append([data.answer1,data.option1_1,data.option1_2,data.option1_3,data.option1_4])
        data.options.append([data.answer2,data.option2_1,data.option2_2,data.option2_3,data.option2_4])
        data.options.append([data.answer3,data.option3_1,data.option3_2,data.option3_3,data.option3_4])
        data.options.append([data.answer4,data.option4_1,data.option4_2,data.option4_3,data.option4_4])
        data.options.append([data.answer5,data.option5_1,data.option5_2,data.option5_3,data.option5_4])
        data.save()
        return data

class AnswerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewAnswer
        fields = ('answers', 'options', 'user')

class GuestSerializer(serializers.ModelSerializer):
    answers = []
    score = 0
    class Meta:
        model = Guest
        fields = ('nickname','user','answer1','answer2','answer3','answer4','answer5','score')

    def create(self, validated_data):
        data = Guest.objects.create(**validated_data)
        data.score = 0
        answer = NewAnswer.objects.get(user=data.user)
        if data.answer1 == answer.answer1:
            data.score += 1
        if data.answer2 == answer.answer2:
            data.score += 1
        if data.answer3 == answer.answer3:
            data.score += 1
        if data.answer4 == answer.answer4:
            data.score += 1
        if data.answer5 == answer.answer5:
            data.score += 1
 
        data.save()
        return data

class CookieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('nickname','score')