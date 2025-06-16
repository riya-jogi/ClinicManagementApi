from rest_framework.response import Response 
from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class DoctorView(GenericAPIView, ListModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['dr_name', 'dr_experience']  # allow sorting by these fields
    ordering = ['dr_name']  # default ordering
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self,request):
    #     doctor = Doctor.objects.all()
    #     serializer = DoctorSerializer(doctor, many = True)
    #     return Response(serializer.data)

    # def dispatch(self, request, *args, **kwargs):
    #     print("=== dispatch() called ===")
    #     print("Authorization Header:", request.headers.get("Authorization"))
    #     return super().dispatch(request, *args, **kwargs)
    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Doctor record inserted"})
        return Response(serializer.errors)
    
class DoctorUDView(GenericAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def put(self,request,id):
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Doctor id":doctor.id, "message":"Doctor record updated"})
        return Response(serializer.errors)
    
    def delete(self,request,id):
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        return Response({"message":"record deleted"})
    

