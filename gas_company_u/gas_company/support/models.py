from django.db import models
from django.contrib.auth.models import User

class SupportRep(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields if needed

    def __str__(self):
        return self.user.username

class SupportRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_requests')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_rep = models.ForeignKey(SupportRep, on_delete=models.SET_NULL, null=True, blank=True, related_name='requests')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.status}"
