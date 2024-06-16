from django.contrib import admin

from api.models.achievement import Achievement
from api.models.answer import Answer
from api.models.article import Article
from api.models.articleFireWorks import ArticleFireWorks
from api.models.articleImage import ArticleImage
from api.models.calculatedTest import CalculatedTest
from api.models.course import Course
from api.models.profile import Profile
from api.models.question import Question
from api.models.test_user_question_answer import TestUserQuestionAnswer
from api.models.studentGroup import StudentGroup
from api.models.test import Test
from api.models.theory import Theory
from api.models.theory_student import TheoryStudent


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)


class ArticleFireWorksAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArticleFireWorks, ArticleFireWorksAdmin)


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer, AnswerAdmin)


class AchievementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Achievement, AchievementAdmin)


class CalculatedTestAdmin(admin.ModelAdmin):
    pass


admin.site.register(CalculatedTest, CalculatedTestAdmin)


class ArticleImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ArticleImage, ArticleImageAdmin)


class TheoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Theory, TheoryAdmin)


class StudentGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(StudentGroup, StudentGroupAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)


class TheoryAndStudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(TheoryStudent, TheoryAndStudentAdmin)


class QuestionAnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(TestUserQuestionAnswer, QuestionAnswerAdmin)
