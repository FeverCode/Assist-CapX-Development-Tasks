from django.db import models

# Create your models here.

class Bug(models.Model):
    DESCRIPTION_CHOICES = [
        ('error', 'Error'),
        ('feature', 'New Feature'),
    ]
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    description = models.TextField()
    bug_type = models.CharField(
        max_length=20,
        choices=DESCRIPTION_CHOICES,
        default='error'
    )
    report_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )
    def __str__(self):
        if self.report_date:
            return f"{self.description} - reported on {self.report_date.strftime('%Y-%m-%d')}"
        return self.description 