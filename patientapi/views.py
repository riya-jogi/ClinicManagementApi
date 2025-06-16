from rest_framework.response import Response 
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PatientView(GenericAPIView, ListModelMixin):
    # queryset = Patient.objects.all()
    # serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [OrderingFilter]
    ordering_fields = ['pname', 'page']  # allow sorting by these fields
    ordering = ['pname']  # default ordering

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    # def get(self,request):
    #     patient = Patient.objects.all()
    #     serializer = PatientSerializer(patient,many = True)
    #     return Response(serializer.data)
    
    def post(self,request):
        serializer = PatientSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Patient record inserted"})
        return Response(serializer.errors)
    
class PatientUDView(GenericAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def put(self,request,id):
        patient = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Patient id":patient.id, "message":"Patient record updated"})
        return Response(serializer.errors)
    
    def delete(self,request,id):
        patient = Patient.objects.get(id=id)
        patient.delete()
        return Response({"message":"record deleted"})
    