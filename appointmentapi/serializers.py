from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def check_availability(self,doctor_id, apmt_date, apmt_time):
        apmt = Appointment.objects.filter(doctor_id=doctor_id, apmt_date=apmt_date,apmt_time=apmt_time)
        if apmt.exists():
            return False
        return True
    
    def validate(self, data):
        doctor_id = data.get('doctor').id
        apmt_date = data.get('apmt_date')
        apmt_time = data.get('apmt_time')

        if not self.check_availability(doctor_id, apmt_date, apmt_time):
            raise serializers.ValidationError("The doctor is not available at the selected date and time.")
        
        return data