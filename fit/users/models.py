from django.db import models

# Create your models here.

class MainUser(models.Model):
    USER_TYPE_CHOICES = [
        ('trainee', 'Trainee'),
        ('trainer', 'Trainer'),
    ]
    name = models.CharField(max_length=15, null= True)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True, blank=True)
    is_completed= models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name if self.name else "User"


