from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.profile import Profile
from api.models.theory import Theory
from api.models.theory_student import TheoryStudent
from api.serializers.theory_studentSerializer import TheoryStudentSerializer


class TheoryAndStudentViewSet(viewsets.ModelViewSet):
    queryset = TheoryStudent.objects.all()
    serializer_class = TheoryStudentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        theory_id = data.get('theoryId')
        student_id = data.get('studentId')
        theory = Theory.objects.get(id=theory_id)
        student = Profile.objects.get(id=student_id)
        if len(TheoryStudent.objects.filter(student=student, theory=theory)) == 0:
            TheoryStudent.objects.create(theory=theory, student=student).save()
        return Response('Created', status=status.HTTP_201_CREATED)
