from rest_framework import serializers

from .models import RetailOutletModel, VisitModel


class RetailOutletListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing retail outlets.

    This serializer is used for serializing retail outlet data for listing purposes.

    Meta:
    - model (Model): The model to serialize.
    - fields (list): The fields to include in the serialized representation.
    """

    class Meta:
        model = RetailOutletModel
        fields = ["pk", "name"]


class VisitSerializer(serializers.ModelSerializer):
    """
    Serializer for visit data.

    This serializer is used for serializing visit data, including its ID and datetime.

    Meta:
    - model (Model): The model to serialize.
    - fields (list): The fields to include in the serialized representation.
    """

    class Meta:
        model = VisitModel
        fields = ["id", "datetime"]


class CoordsSerializer(serializers.Serializer):
    """
    Serializer for geographical coordinates.

    This serializer is used for validating and serializing latitude and longitude coordinates.

    Fields:
    - latitude (FloatField): The latitude coordinate (required).
    - longitude (FloatField): The longitude coordinate (required).
    """

    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)


class CreateVisitSerializer(serializers.Serializer):
    """
    Serializer for creating a new visit.

    This serializer is used for validating and serializing data when creating a new visit.

    Fields:
    - phone_number (CharField): The phone number of the employee (max length 255, required).
    - retail_outlet (PrimaryKeyRelatedField): The retail outlet associated with the visit (required).
    - coords (CoordsSerializer): Geographical coordinates of the visit (provided by CoordsSerializer).
    """

    phone_number = serializers.CharField(max_length=255, required=True)
    retail_outlet = serializers.PrimaryKeyRelatedField(
        queryset=RetailOutletModel.objects.all(),
        required=True,
    )
    coords = CoordsSerializer()
