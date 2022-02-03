from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .serializers import UserSerializer
from .models import UserManager


def get_params(request):
    return request.data | request.query_params.dict()

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    params = get_params(request)
    email, password = params['email'], params['password']
    email = UserManager.normalize_email(email)
    user = authenticate(email=email, password=password)

    if not user:
        raise AuthenticationFailed('Invalid credentials')

    token = RefreshToken.for_user(user) 

    data = {
        "auth_token": str(token.access_token)  # should provide refresh token as well
    }

    return Response(data)


class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request):
        params = request.data.dict() | request.query_params.dict()
        serializer = self.get_serializer(data=params)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = {
            "message": "Account created successfully",
            "auth_token": str(token.access_token)
        }
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
