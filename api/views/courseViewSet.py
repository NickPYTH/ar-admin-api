from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.course import Course
from api.models.profile import Profile
from api.models.theory import Theory
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

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        courses = Course.objects.all()
        response = []
        for course in courses:
            current_points = 0
            theories = course.theories.all()
            for theory in theories:
                if len(TheoryStudent.objects.filter(student=profile, theory=theory)) > 0:
                    current_points += 1
            tests = course.tests.all()
            max_points = len(theories) + len(tests)
            course_data = {
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "currentPoints": current_points,
                "maxPoints": max_points
            }
            response.append(course_data)

        return Response(response, status=status.HTTP_200_OK)
