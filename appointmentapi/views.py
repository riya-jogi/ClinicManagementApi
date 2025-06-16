from rest_framework.response import Response 
from .serializers import AppointmentSerializer
from .models import Appointment
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

class AppointmentView(GenericAPIView, ListModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter]
    ordering_fields = ['apmt_date', 'patient']  # allow sorting by these fields
    ordering = ['patient']  # default ordering

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    #   def get(self,request):
    #     apmt = Appointment.objects.all()
    #     serializer = AppointmentSerializer(apmt,many = True)
    #     return Response(serializer.data)
    
    def post(self,request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Appointment record inserted"})
        return Response(serializer.errors)
    
class AppointmentUDView(GenericAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def put(self,request,id):
        apmt = Appointment.objects.get(id=id)
        serializer = AppointmentSerializer(apmt,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Appointment id":apmt.id, "message":"Appointment record upadated"})
        return Response(serializer.errors)
    
    def delete(self,request,id):
        apmt = Appointment.objects.get(id=id)
        apmt.delete()
        return Response({"message":"record deleted"})
