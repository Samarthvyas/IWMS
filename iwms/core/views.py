from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def report_waste(request):
    return render(request,'report_waste.html')

def my_reports(request):
    return render(request,'my_reports.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def all_reports(request):
    return render(request,'all_reports.html')

def admin_report_detail(request, report_id):
    return render(
        request,
        "report_detail.html",
        {
            "report_id": report_id
        }
    )

def users_page(request):
    return render(request, "users.html")

def about(request):
    return render(request, "about.html")