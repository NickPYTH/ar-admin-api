from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

from .models import *


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


admin.site.register(TheoryAndStudent, TheoryAndStudentAdmin)












