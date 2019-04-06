from rest_framework import authentication


class JWTAuthentication(authentication.TokenAuthentication):

    keyword = 'JWT'
