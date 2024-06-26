from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.course import Course
from api.models.profile import Profile
from api.models.theory import Theory
from api.models.test import Test
from api.models.calculatedTest import CalculatedTest
from api.models.theory_student import TheoryStudent
from api.serializers.courseSerializer import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=kwargs.get("pk"))
        serializer = CourseSerializer(course, context={'request': request})

        for theory in serializer["theories"].value:
            if len(TheoryStudent.objects.filter(student=profile, theory=Theory.objects.get(id=theory["id"]))) > 0:
                theory["isRead"] = True
            else:
                theory["isRead"] = False

        for test in serializer['tests'].value:
            test_model = Test.objects.get(id=test['id'])
            best_test_result = None
            if CalculatedTest.objects.filter(user=request.user, test=test_model).count() != 0:
                best_test_result = CalculatedTest.objects.filter(user=request.user, test=test_model).order_by(
                    "-user_points").first()
            if best_test_result is not None:
                test['maxPoints'] = best_test_result.max_points
                test['userPoints'] = best_test_result.user_points
            else:
                max_points = 0
                for question in test_model.questions.all():
                    max_points += question.points
                test['maxPoints'] = max_points
                test['userPoints'] = 0

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        courses = Course.objects.all()
        response = []
        for course in courses:
            max_points = 0
            current_points = 0
            theories = course.theories.all()
            for theory in theories:
                if len(TheoryStudent.objects.filter(student=profile, theory=theory)) > 0:
                    current_points += theory.points
                max_points += theory.points
            for test in course.tests.all():
                test_points = 0
                for question in test.questions.all():
                    test_points += question.points
                max_points += test_points
                best_test_result = None
                if CalculatedTest.objects.filter(user=request.user, test=test).count() != 0:
                    best_test_result = CalculatedTest.objects.filter(user=request.user, test=test).order_by(
                        "-user_points").first()
                if best_test_result is not None:
                    if test.test.pass_line <= (best_test_result.user_points / best_test_result.max_points):
                        current_points += best_test_result.user_points

            course_data = {
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "currentPoints": current_points,
                "maxPoints": max_points
            }
            response.append(course_data)

        return Response(response, status=status.HTTP_200_OK)
