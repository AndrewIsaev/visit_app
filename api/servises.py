from rest_framework import status
from rest_framework.response import Response

from api.models import EmployeeModel


def get_access(retail_outlet, employee_phone_number):
    """
       Checks if an employee is associated with the specified retail outlet.

       Function verifies whether an employee with the provided phone number is associated with the given retail outlet.
       It performs a database lookup to match the employee's phone number and the retail outlet's assigned employee.

       Parameters:
       - retail_outlet: RetailOutletModel object representing the retail outlet.
       - employee_phone_number: Phone number of the employee to be checked.

       Returns:
       - Response: A Response object with an error message and HTTP status code.
         - If the employee is not associated with the retail outlet,
         it returns a 400 Bad Request response with an error message.
         - If the employee or retail outlet is not found in the database,
         it returns a 400 Bad Request response with an appropriate error message.
   """
    try:
        employee = EmployeeModel.objects.get(phone_number=employee_phone_number)
        if retail_outlet.employee != employee:
            return Response(
                {"error": "Этот работник не привязан к указанной торговой точке."},
                status=status.HTTP_400_BAD_REQUEST,

            )
    except EmployeeModel.DoesNotExist:
        return Response(
            {"error": "Работник или торговая точка не найдены."},
            status=status.HTTP_400_BAD_REQUEST,
        )
