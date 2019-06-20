
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drive import views
from django.conf import settings
from django.conf.urls.static import static
from drive.api.views import UserCreateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/drive/', include(('drive.api.urls', 'drive.api'), namespace='api-drive')),
    path('registration/', UserCreateView.as_view(), name='user-registration'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
