from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('REPAIR', 'Repair'),
        ('INSTALLATION', 'Installation'),
        ('MAINTENANCE', 'Maintenance'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES)
    details = models.TextField()
    file = models.FileField(upload_to='requests/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} by {self.user.username} - {self.status}"
