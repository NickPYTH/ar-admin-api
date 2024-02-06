from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

admin.site.site_header = "AR Администрирование"
admin.site.site_title = "AR Администрирование"
admin.site.index_title = "Добро пожаловать в панель администрирования"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls')),
]
