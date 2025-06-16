from rest_framework.response import Response
from appointmentapi.models import Appointment 
from .serializers import MedicalReportSerializer
from .models import MedicalReport
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MedicalReportView(GenericAPIView, ListModelMixin):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter]
    ordering_fields = ['patient', 'doctor']  # allow sorting by these fields
    ordering = ['patient']  # default ordering

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self,request):
    #     medi_rpt = MedicalReport.objects.all()
    #     serializer = MedicalReportSerializer(medi_rpt, many =True)
    #     return Response(serializer.data)
        
    def post(self, request):
        serializer = MedicalReportSerializer(data=request.data)
        if serializer.is_valid():
            doctor = serializer.validated_data['doctor']
            patient = serializer.validated_data['patient']

            if not Appointment.objects.filter(doctor=doctor, patient=patient).exists():
                return Response({"error": "This doctor has not seen this patient."})
            serializer.save()
            return Response({"message": "Medical report inserted"})
        return Response(serializer.errors)

class MedicalReportUDView(GenericAPIView):
    serializer_class = MedicalReportSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            report = MedicalReport.objects.get(id=id)
        except MedicalReport.DoesNotExist:
            return Response({"error": "Medical report not found."})

        doctor_id = request.data.get('doctor')
        patient_id = request.data.get('patient')

        if str(report.doctor.id) != str(doctor_id):
            return Response({"error": "Doctor can only update their own records."})

        if not Appointment.objects.filter(doctor_id=doctor_id, patient_id=patient_id).exists():
            return Response({"error": "This doctor has not seen this patient."})

        serializer = MedicalReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Medical report id": report.id, "message": "Updated medical report"})
        return Response(serializer.errors)

    def delete(self, request, id):
        report = MedicalReport.objects.get(id=id)
        report.delete()
        return Response({"message":"Medical report deleted"})