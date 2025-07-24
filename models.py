from django.db import models
from django.contrib.auth.models import AbstractUser

#user model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"



#Assignment Model

class Assignment(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.title
    

    
#submission model

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    content = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)  # track creation time only

    class Meta:
        unique_together = ('assignment', 'student')  # one submission per student per assignment

    def __str__(self):
        return f"{self.assignment.title} - {self.student.username}"
