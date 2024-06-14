from rest_framework import serializers

from api.models.theory_student import TheoryStudent
from api.serializers.profileSerializer import ProfileSerializer
from api.serializers.theorySerializer import TheorySerializer


class TheoryStudentSerializer(serializers.HyperlinkedModelSerializer):
    theory = TheorySerializer()
    student = ProfileSerializer()

    class Meta:
        model = TheoryStudent
        fields = ('theory', 'student')
