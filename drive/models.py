from django.db import models
from django.conf import settings
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
# Create your models here.
class Drive(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/%user/files/%Y/%m/%D/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/%user/images/%Y/%m/%D/', blank=True, null=True)

    @property
    def owner(self):
        return self.user

    def url(self, request=None):
        return api_reverse("api-drive:drive-item", kwargs={'pk': self.pk}, request=request)
