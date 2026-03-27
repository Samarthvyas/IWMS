from rest_framework import generics, permissions
from .models import WasteReport
from .serializers import WasteReportSerializer
from users.models import User

# Create Report
class CreateReportView(generics.CreateAPIView):
    queryset = WasteReport.objects.all()
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = User.objects.first()  # temporary fix
        serializer.save(user=self.request.user)


# User: View own reports
class UserReportsView(generics.ListAPIView):
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = User.objects.first()   # ✅ force valid user
        return WasteReport.objects.filter(user=user)


# Admin: View all reports
class AllReportsView(generics.ListAPIView):
    queryset = WasteReport.objects.all()
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.AllowAny]