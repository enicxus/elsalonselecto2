
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
@permission_classes((IsAuthenticated))
@api_view (['post'])
def login (request):
    data = JSONParser().parase(request)

    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response ("usuario invalido")
    #validamos la contra
    pass_valido =check_password(password,user.password)
    if not pass_valido:
        return Response ("password incorrecta")
    #permitir o recuperar al token
    token, created = Token.objects.get_or_create(user.user)
    #print (token.key)
    return Response(token.key) 