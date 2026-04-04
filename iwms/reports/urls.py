from django.urls import path
from .views import CreateReportView, UserReportsView, AllReportsView, UpdateReportStatusView

urlpatterns = [
    path('create/', CreateReportView.as_view()),
    path('my-reports/', UserReportsView.as_view()),
    path('all-reports/', AllReportsView.as_view()),
    path('update/<int:pk>/', UpdateReportStatusView.as_view()),
]