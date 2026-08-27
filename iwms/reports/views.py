from rest_framework import generics, permissions 
from rest_framework.permissions import IsAuthenticated
from .models import WasteReport
from .serializers import WasteReportSerializer
from users.models import User
from ai_model.predict import predict_image
import logging

logger = logging.getLogger(__name__)

# Create Report
class CreateReportView(generics.CreateAPIView):
    queryset = WasteReport.objects.all()
    serializer_class = WasteReportSerializer
    permission_classes = [IsAuthenticated]
 
    def perform_create(self, serializer):

        report = serializer.save(user=self.request.user)

        try:
            predicted_class, confidence = predict_image(report.image.path)

            report.waste_type = predicted_class.lower()
            report.ai_confidence = confidence

            # Automatic Priority Assignment
            if report.waste_type == "hazardous":
                report.priority = "high"

            elif report.waste_type == "wet":
                report.priority = "medium"

            elif report.waste_type == "dry":
                report.priority = "low"

            report.save()

        except Exception:
            logger.exception("AI Prediction Error")


# User: View own reports
class UserReportsView(generics.ListAPIView):
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WasteReport.objects.filter(user=self.request.user).order_by('-created_at')


# Admin: View all reports
class AllReportsView(generics.ListAPIView):
    queryset = WasteReport.objects.all()
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.IsAdminUser]

class UpdateReportStatusView(generics.UpdateAPIView):
    queryset = WasteReport.objects.all()
    serializer_class = WasteReportSerializer
    permission_classes = [permissions.IsAdminUser]    