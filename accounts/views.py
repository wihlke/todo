# from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserManager



def get_params(request):
    return request.data | request.query_params.dict()

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    params = get_params(request)
    email, password = params['email'], params['password']

    email = UserManager.normalize_email(email)
    user = User.objects.filter(email=email).first()

    if not (user and user.check_password(password)):
        raise AuthenticationFailed('Invalid credentials')

    token = RefreshToken.for_user(user) 

    data = {
        "auth_token": str(token.access_token)  # should provide refresh token as well
    }

    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    params = get_params(request)
    serializer = UserRegisterSerializer(data=params, context=dict(request=request))
    serializer.is_valid(raise_exception=True)

    user = serializer.create(serializer.data)
    token = RefreshToken.for_user(user) 

    data = {
        "message": "Account created successfully",
        "auth_token": str(token.access_token)
    }

    response = Response(data)
    user.save()  # Delay save if there's an issue
    return response
