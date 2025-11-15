from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access")
        print("Access token from cookie:", access_token)

        if not access_token:
            return None  # DRF returns "not provided"

        try:
            validated_token = self.get_validated_token(access_token)
        except Exception:
            raise exceptions.AuthenticationFailed("Invalid or expired token")

        user = self.get_user(validated_token)
        return (user, validated_token)
