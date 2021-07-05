from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User


from ..serializers import AISSerializer
from ..models.ais_model import AIS
 
class AisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AIS to be added, viewed or edited.
    """
    queryset = AIS.objects.all()
    serializer_class = AISSerializer
    permission_classes = [permissions.IsAuthenticated]