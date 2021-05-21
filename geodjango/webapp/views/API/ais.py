from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

from ...serializers import AISSerializer
from ...models.ais import AIS
 
class AisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AIS.objects.all()
    serializer_class = AISSerializer
    permission_classes = [permissions.IsAuthenticated]