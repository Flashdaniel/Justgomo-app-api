from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import BillSerializer
from .models import DashboardBill


class ListDashboardBill(generics.ListAPIView):
    """Authenticated User can list the billing list"""

    queryset = DashboardBill.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer


class CreateDashboardBill(generics.CreateAPIView):
    """Authenticated and also most be admin User can Create a bill"""

    queryset = DashboardBill.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = BillSerializer


class RetrievesDashboard(generics.RetrieveAPIView):
    """Authenticated User can retrieve a bill"""

    queryset = DashboardBill.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer


class UpdateDashboardBill(generics.UpdateAPIView):
    """Authenticated and also most be admin User can update a bill"""

    queryset = DashboardBill.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BillSerializer


class DestroyDashboardBill(generics.DestroyAPIView):
    """Authenticated and also most be admin User can destroy a bill"""

    queryset = DashboardBill.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BillSerializer
