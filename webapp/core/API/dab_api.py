from rest_framework import permissions, viewsets
from django.contrib.auth.models import User

from ..serializers import dabSerializer
from ..models import dabModel
 
class DabViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AIS to be added, viewed or edited.
    """
    queryset = dabModel.objects.all()
    serializer_class = dabSerializer
    permission_classes = [permissions.IsAuthenticated]