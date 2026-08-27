from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='frontend_login'),
    path("register/", views.register_view, name='frontend_register'),
    path("dashboard/", views.dashboard, name='frontend_dashboard'),
    path("report-waste/", views.report_waste, name='frontend_report_waste'),
    path("my-reports/", views.my_reports, name="frontend_my_reports"),
    path("admin-dashboard/",views.admin_dashboard,name="frontend_admin_dashboard"),
    path("all-reports/", views.all_reports,name="frontend_all_reports"),
    path(
    "admin-report/<int:report_id>/",
    views.admin_report_detail,
    name="frontend_admin_report_detail"),
    
    path("users/",
    views.users_page,
    name="frontend_users"),

    path("about/",
    views.about,
    name="frontend_about"),

]