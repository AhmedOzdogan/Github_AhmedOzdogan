from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from blog_api.models import User  # your custom user model


def _get_tokens_for_user(user: User):
    """
    Helper to create refresh + access tokens for a user.
    """
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class CookieLoginView(APIView):
    """
    Login with username OR email.
    Set JWTs in HttpOnly cookies.
    Return only user info in body.
    """

    def post(self, request):
        login_value = request.data.get("username")
        password = request.data.get("password")

        if not login_value or not password:
            return Response(
                {"detail": "Username/email and password required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Try email first
        user_obj = User.objects.filter(email=login_value).first()
        actual_username = user_obj.username if user_obj else login_value

        user = authenticate(username=actual_username, password=password)

        if not user:
            return Response(
                {"detail": "Invalid username/email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if user.blocked: #type: ignore
            return Response(
                {"detail": "Your account is blocked."},
                status=status.HTTP_403_FORBIDDEN,
            )

        tokens = _get_tokens_for_user(user)  #type: ignore

        response = Response(
            {
                "user": {
                    "id": user.id, #type: ignore
                    "username": user.username,
                    "email": user.email,
                    "role": user.role, #type: ignore
                    "blocked": user.blocked, #type: ignore
                }
            },
            status=status.HTTP_200_OK,
        )

        # ⚠ In production set secure=True and adjust samesite
        response.set_cookie(
            key="access",
            value=tokens["access"],
            httponly=True,
            secure=False,      # True on HTTPS
            samesite="Lax",  # Adjust as needed
            # domain="localhost",  # adjust if needed
            max_age=60 * 5,    # match ACCESS_TOKEN_LIFETIME
        )

        response.set_cookie(
            key="refresh",
            value=tokens["refresh"],
            httponly=True,
            secure=False,      # True on HTTPS
            samesite="Lax",  # Adjust as needed
            # domain="localhost",  # adjust if needed
            max_age=60 * 60 * 24 * 7,  # 7 days
        )

        return response


class CookieRefreshView(APIView):
    """
    Use refresh token from HttpOnly cookie
    to issue a new access token (set in cookie again).
    """

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh")
        if not refresh_token:
            return Response({"detail": "No refresh token"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            refresh = RefreshToken(refresh_token)
        except Exception:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)

        new_access = refresh.access_token

        response = Response(
            {"detail": "Token refreshed"},
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key="access",
            value=str(new_access),
            httponly=True,
            secure=False,   # True in prod
            samesite="Lax",  # Adjust as needed
            # domain="localhost",  # adjust if needed
            max_age=60 * 5,
        )

        return response


class CookieLogoutView(APIView):
    """
    Clear auth cookies (access + refresh).
    """

    def post(self, request):
        response = Response({"detail": "Logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
