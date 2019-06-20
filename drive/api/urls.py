from .views import DriveItemView, DriveListView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<pk>', DriveItemView.as_view(), name='drive-item'),
    path('', DriveListView.as_view(), name='drive-list'),
    
]
