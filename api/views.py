from rest_framework import generics, status
from rest_framework.response import Response

from api.models import EmployeeModel, RetailOutletModel, VisitModel
from api.serializers import (
    CreateVisitSerializer,
    RetailOutletListSerializer,
    VisitSerializer,
)
from api.servises import get_access


# Create your views here.
class ListRetailOutletsView(generics.ListAPIView):
    """
    API view to list retail outlets filtered by an employee's phone number.

    This view allows clients to retrieve a list of retail outlets based on the provided employee's phone number.

    Parameters:
    - queryset: Queryset of all retail outlets.
    - serializer_class: Serializer class to serialize the retail outlets.

    Methods:
    - get_queryset: Filter the queryset based on the provided phone number.
    """

    queryset = RetailOutletModel.objects.all()
    serializer_class = RetailOutletListSerializer

    def get_queryset(self):
        phone_number = self.request.data.get("phone_number")
        return RetailOutletModel.objects.filter(employee__phone_number=phone_number)


class CreateVisitView(generics.CreateAPIView):
    """
    API view to create a visit to a retail outlet.

    This view allows clients to create a visit to a retail outlet. It validates the provided data and ensures
     that the employee is associated with the specified retail outlet.

    Parameters:
    - serializer_class: Serializer class for creating visits.

    Methods:
    - create: Process the creation of a new visit, including data validation and association checks.
    """

    serializer_class = CreateVisitSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        retail_outlet = serializer.validated_data["retail_outlet"]
        coords = serializer.validated_data["coords"]

        not_authorize = get_access(retail_outlet=retail_outlet, employee_phone_number=phone_number)
        if not_authorize:
            return not_authorize

        new_visit = VisitModel(
            retail_outlet_id=retail_outlet.pk,
            latitude=coords["latitude"],
            longitude=coords["longitude"],
        )
        new_visit.save()

        serialized_visit = VisitSerializer(new_visit)

        return Response(serialized_visit.data, status=status.HTTP_201_CREATED)
