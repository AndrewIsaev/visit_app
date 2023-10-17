from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    """
    Model representing an employee.

    Fields:
    - name (CharField): The name of the employee.
    - phone_number (CharField): The phone number of the employee.

    Methods:
    - __str__(): Returns a string representation of the employee.

    Meta:
    - verbose_name (str): Human-readable singular name for the model.
    - verbose_name_plural (str): Human-readable plural name for the model.
    """

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class RetailOutletModel(models.Model):
    """
    Model representing a retail outlet or store.

    Fields:
    - name (CharField): The name of the retail outlet.
    - employee (ForeignKey): A reference to the associated employee.

    Methods:
    - __str__(): Returns a string representation of the retail outlet.

    Meta:
    - verbose_name (str): Human-readable singular name for the model.
    - verbose_name_plural (str): Human-readable plural name for the model.
    """

    name = models.CharField(max_length=255)
    employee = models.ForeignKey("api.EmployeeModel", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Торговая точка"
        verbose_name_plural = "Торговые точки"


class VisitModel(models.Model):
    """
    Model representing a visit to a retail outlet.

    Fields:
    - datetime (DateTimeField): The date and time of the visit.
    - retail_outlet (ForeignKey): A reference to the visited retail outlet.
    - latitude (FloatField): The latitude coordinate of the visit.
    - longitude (FloatField): The longitude coordinate of the visit.

    Methods:
    - __str__(): Returns a string representation of the visit.

    Meta:
    - verbose_name (str): Human-readable singular name for the model.
    - verbose_name_plural (str): Human-readable plural name for the model.
    """

    datetime = models.DateTimeField(auto_now_add=True)
    retail_outlet = models.ForeignKey("api.RetailOutletModel", on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.retail_outlet.name}"

    class Meta:
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"
