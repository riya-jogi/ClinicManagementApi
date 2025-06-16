from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import RegisterView, LoginView, ProtectedView

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentaion",
      default_version='v1',
      description="Clinic & Patient API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('protected/', ProtectedView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]
# clinicauthorization/urls.py



