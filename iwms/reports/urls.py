from django.urls import path
from .views import CreateReportView, UserReportsView, AllReportsView

urlpatterns = [
    path('create/', CreateReportView.as_view()),
    path('my-reports/', UserReportsView.as_view()),
    path('all-reports/', AllReportsView.as_view()),
]