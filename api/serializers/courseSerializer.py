from rest_framework import serializers

from api.models.course import Course
from api.serializers.testSerializer import TestSerializer
from api.serializers.theorySerializer import TheorySerializer


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    theories = TheorySerializer(many=True)
    tests = TestSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'theories', 'tests')
