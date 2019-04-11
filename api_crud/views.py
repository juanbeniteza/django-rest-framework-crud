from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from rest_auth.models import TokenModel
from rest_auth.views import LoginView
from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
from django.contrib.auth.models import User

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2')
)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        content = {
            "details": "Registered"
        }
        return Response(content,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)

        complete_signup(self.request._request, user, None, None)
        return user


class CustomLoginView(LoginView):
    
    def get_response(self):
        orginal_response = super().get_response()

        custom_response = {"user": {
            "username": self.user.username,
            "email": self.user.email
        }}
        
        orginal_response.data.update(custom_response)
        return orginal_response
