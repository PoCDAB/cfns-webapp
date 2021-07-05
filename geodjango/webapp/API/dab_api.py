from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User

from ..serializers import DABSerializer
from ..models.dab_model import DAB
 
class DabViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AIS to be added, viewed or edited.
    """
    queryset = DAB.objects.all()
    serializer_class = DABSerializer
    permission_classes = [permissions.IsAuthenticated]