from rest_framework import permissions, viewsets
from django.contrib.auth.models import User

from ..serializers import lorawanSerializer
from ..models import lorawanModel
 
class lorawanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AIS to be added, viewed or edited.
    """
    queryset = lorawanModel.objects.all()
    serializer_class = lorawanSerializer
    permission_classes = [permissions.IsAuthenticated]