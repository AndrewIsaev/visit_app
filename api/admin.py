from django.contrib import admin

from api.models import EmployeeModel, RetailOutletModel, VisitModel


# Register your models here.
@admin.register(EmployeeModel)
class Admin(admin.ModelAdmin):
    """
    Administrative interface for the EmployeeModel.

    Allows administrators to manage employees.

    Parameters:
    - search_fields (list): List of fields to search for employees.
    """

    list_display = ("name", "phone_number")
    search_fields = ["name"]


@admin.register(RetailOutletModel)
class RetailOutletAdmin(admin.ModelAdmin):
    """
    Administrative interface for the RetailOutletModel.

    Allows administrators to manage retail outlets.

    Parameters:
    - search_fields (list): List of fields to search for retail outlets.
    """

    list_display = ("name", "employee")
    search_fields = ["name"]


@admin.register(VisitModel)
class VisitAdmin(admin.ModelAdmin):
    """
    Administrative interface for the VisitModel.

    Allows administrators to manage visits to retail outlets.

    Parameters:
    - list_display (tuple): List of fields displayed in the list of visits.
    - search_fields (list): List of fields to search for visits.
    """

    list_display = ("datetime", "retail_outlet", "latitude", "longitude")
    search_fields = ["retail_outlet__name", "retail_outlet__employee__name"]
