
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
