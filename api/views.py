from django.http import FileResponse
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from .models import *


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        user_serialized = UserSerializer(user)
        response = user_serialized.data
        good = CalculatedTest.objects.filter(user=user, result=True)
        bad = CalculatedTest.objects.filter(user=user, result=False)
        response['goodTests'] = good.count()
        response['badTests'] = bad.count()
        return Response(response, status=200)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class ArticleFireWorksViewSet(viewsets.ModelViewSet):
    queryset = ArticleFireWorks.objects.all()
    serializer_class = ArticleFireWorksSerializer
    permission_classes = [IsAuthenticated]


class CalculatedTestViewSet(viewsets.ModelViewSet):
    queryset = CalculatedTest.objects.all()
    serializer_class = CalculatedTestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        test = CalculatedTest()
        test.test = Test.objects.get(id=data['test_id'])
        test.user = request.user
        test.result = data['result']
        test.save()
        return Response(status=200)


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        image = ArticleImage.objects.get(name="image_" + kwargs.get("pk"))
        response = FileResponse(image.image)
        return response
    

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return self;


class TheoryAndStudentViewSet(viewsets.ModelViewSet):
    queryset = TheoryAndStudent.objects.all()
    serializer_class = TheoryAndStudentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        theory_id = data.get('theoryId')
        student_id = data.get('studentId')
        theory = Theory.objects.get(id=theory_id)
        student = Profile.objects.get(id=student_id)
        if len(TheoryAndStudent.objects.filter(student=student, theory=theory)) == 0:
            TheoryAndStudent.objects.create(theory=theory, student=student).save()
        return Response('Created', status=status.HTTP_201_CREATED)
