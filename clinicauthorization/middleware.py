
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_auth = JWTAuthentication()

    def __call__(self, request):
        try:
            print("Headers:", request.headers)
            user_auth_tuple = self.jwt_auth.authenticate(request)

            if user_auth_tuple is not None:
                user, token = user_auth_tuple
                if not User.objects.filter(id=user.id).exists():
                    return JsonResponse({'detail': 'User not found in DB'}, status=401)
                
                request.user = user
                request.auth = token
                print(f"[Middleware] Authenticated user: {user}")
            else:
                request.user = None
                print("[Middleware] No user found in token")
        except (AuthenticationFailed, InvalidToken) as e:
            print("[Middleware] JWT Error:", str(e))
            return JsonResponse({'detail': str(e)}, status=401)
        
        return self.get_response(request)



# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.exceptions import AuthenticationFailed
# from django.http import JsonResponse
# from clinicauthorization.models import RegisterUser  # replace with your app name
# from django.utils.deprecation import MiddlewareMixin

# class CustomJWTMiddleware(MiddlewareMixin):
#     def __init__(self, get_response=None):
#         self.get_response = get_response
#         self.jwt_auth = JWTAuthentication()

#     def process_request(self, request):
#         try:
#             print(request.headers)
#             user_auth_tuple = self.jwt_auth.authenticate(request)
#             print(request.headers)
#             if user_auth_tuple:
#                 user, token = user_auth_tuple

#                 # Use RegisterUser model, not default Django user
#                 try:
#                     db_user = RegisterUser.objects.get(email=user.email)
#                     request.user = db_user
#                     request.auth = token
#                     print(f"[CustomJWTMiddleware] Authenticated: {db_user.email}")
#                 except RegisterUser.DoesNotExist:
#                     print("[CustomJWTMiddleware] User not found in RegisterUser")
#                     return JsonResponse({'detail': 'User not found.'}, status=401)
#             else:
#                 request.user = None
#                 print("[CustomJWTMiddleware] No user authenticated")

#         except AuthenticationFailed as e:
#             print("[CustomJWTMiddleware] JWT error:", str(e))
#             return JsonResponse({'detail': 'Invalid or expired token'}, status=401)

#         return None  
