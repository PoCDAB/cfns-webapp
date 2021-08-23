from rest_framework import permissions, viewsets
from django.contrib.auth.models import User


from ..serializers import aisSerializer
from ..models import aisDecodedModel
 
class AisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AIS to be added, viewed or edited.
    """
    queryset = aisDecodedModel.objects.all()
    serializer_class = aisSerializer
    permission_classes = [permissions.IsAuthenticated]