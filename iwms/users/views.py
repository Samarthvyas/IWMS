from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class AllUsersView(generics.ListAPIView):

    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):

        users = self.get_queryset()

        data = []

        for user in users:

            data.append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "is_staff": user.is_staff,
                "date_joined": user.date_joined,
            })

        return Response(data)