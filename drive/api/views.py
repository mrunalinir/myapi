
from django.db.models import Q
from rest_framework import generics, mixins
from drive.models import Drive
from .permissions import IsOwnerOrNoAccess
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import DriveSerializer, UserSerializer
from django.contrib.auth.models import User

class DriveListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field    = 'pk'
    serializer_class = DriveSerializer
    permission_classes = [IsAuthenticated]
#    queryset        =  Drive.objects.all()

    def get_queryset(self):
        user = self.request.user
        qs = Drive.objects.filter(user = user)
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(description__icontains=query)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def post(self, request, *args, **kwargs):
        drive = self.create(request, *args, **kwargs)
        return d


    def serializer_context(self, *args, **kwargs):
        return {"request":self.request}

class DriveItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrNoAccess]
    lookup_field    = 'pk' # url(r'?P<pk>\d+')
    serializer_class = DriveSerializer

#    queryset        =  Drive.objects.all()


    def get_queryset(self):
        return Drive.objects.all()

    def serializer_context(self, *args, **kwargs):
        return {"request":self.request}

'''    def get_object(self):
        pk = self.kwargs.get('pk')
        return Drive.objects.get(pk=pk)'''

class UserCreateView(generics.CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    qs = User.objects.all()
