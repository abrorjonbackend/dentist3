from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'firstName', 'lastName', 'birthDate', 'address', 'appointmentDate', 'appointmentTime', 'price', 'givenPrice', 'doctor', 'tel', 'description']
        read_only_fields = ['id']  # ID will be automatically handled
