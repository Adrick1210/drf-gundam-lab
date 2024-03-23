from .models import MobileSuit
from rest_framework import viewsets, permissions
from .serializers import MobileSuitSerializer

class MobileSuitViewSet(viewsets.ModelViewSet):
    queryset=MobileSuit.objects.all()
    serializer_class=MobileSuitSerializer
    permission_classes=[permissions.AllowAny]