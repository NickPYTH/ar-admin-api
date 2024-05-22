from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'achievements', views.AchievementViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'articlesFireWorks', views.ArticleFireWorksViewSet)
router.register(r'calculatedTests', views.CalculatedTestViewSet)
router.register(r'articleImages', views.ArticleImageViewSet)
router.register(r'courses', views.CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
