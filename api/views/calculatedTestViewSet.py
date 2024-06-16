from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.answer import Answer
from api.models.calculatedTest import CalculatedTest
from api.models.question import Question
from api.models.test_user_question_answer import TestUserQuestionAnswer
from api.models.test import Test
from api.serializers.calculatedTestSerializer import CalculatedTestSerializer


class CalculatedTestViewSet(viewsets.ModelViewSet):
    queryset = CalculatedTest.objects.all()
    serializer_class = CalculatedTestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        test = CalculatedTest()
        test.test = Test.objects.get(id=data['test_id'])
        test.user = request.user
        test.save()
        question_answer_list = []
        maxPoints = 0
        userPoints = 0
        for el in data['result']:
            question = Question.objects.get(id=el['questionId'])
            maxPoints += question.points
            answer = Answer.objects.get(id=el['answerId'])
            if answer.isCorrect:
                userPoints += question.points
            question_answer = TestUserQuestionAnswer.objects.create(user=test.user,
                                                                    question=question,
                                                                    answer=answer)
            question_answer.save()
            question_answer_list.append(question_answer)
            question_answer.save()
        test.test_user_question_answer_list.set(question_answer_list)
        test.save()
        is_passed = test.test.pass_line <= (userPoints / maxPoints)
        return Response({"isPassed": is_passed, "maxPoints": maxPoints, "userPoints": userPoints}, status=201)
