from django.db import models

class Patient(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    address = models.TextField()
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    givenPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # make optional
    doctor = models.TextField()
    tel = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
