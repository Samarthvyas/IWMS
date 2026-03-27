from django.db import models
from django.conf import settings

class WasteReport(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    WASTE_TYPE_CHOICES = (
        ('wet', 'Wet'),
        ('dry', 'Dry'),
        ('hazardous', 'Hazardous'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='waste_images/')
    location = models.CharField(max_length=255)

    latitude = models.FloatField()
    longitude = models.FloatField()

    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE_CHOICES, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} - {self.user}"