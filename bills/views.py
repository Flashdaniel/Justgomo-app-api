from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import BillSerializer, PayedBillSerializer
from .models import Bill, PayedBill


class ListBill(generics.ListAPIView):
    """Authenticated User can list the billing list"""

    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BillSerializer


class CreateBill(generics.CreateAPIView):
    """Authenticated and also most be admin User can Create a bill"""

    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = BillSerializer


class RetrievesBill(generics.RetrieveAPIView):
    """Authenticated user can retrieve a bill"""

    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BillSerializer


class UpdateBill(generics.UpdateAPIView):
    """Authenticated and also most be admin User can update a bill"""

    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BillSerializer


class DestroyBill(generics.RetrieveUpdateDestroyAPIView):
    """Authenticated and also most be admin User can destroy a bill"""

    queryset = Bill.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BillSerializer


class ListPayedBill(generics.ListAPIView):
    """Authenticated User can list the payed billing list"""

    queryset = PayedBill.objects.all()
    # permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = PayedBillSerializer


class CreatePayedBill(generics.CreateAPIView):
    """Authenticated User can Create a payed bill"""

    queryset = PayedBill.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PayedBillSerializer


class RetrievesPayedBill(generics.RetrieveAPIView):
    """Authenticated user can retrieve a payed bill"""

    queryset = PayedBill.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PayedBillSerializer


class UpdatePayedBill(generics.UpdateAPIView):
    """Authenticated User can update a payed bill"""

    queryset = PayedBill.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PayedBillSerializer
