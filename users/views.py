from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=UserSerializer)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)




# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     user = request.user
#     return Response({
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#     })



# class ProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     @extend_schema(
#         responses=RegisterSerializer
#     )
#     def get(self, request):
#         serializer = RegisterSerializer(request.user)
#         return Response(serializer.data)
