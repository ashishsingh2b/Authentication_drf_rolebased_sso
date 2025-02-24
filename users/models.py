from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Role(models.TextChoices):
    ENGINEER = "Engineer","Engineer"
    COUSTOMER= "Customer","Customer"
    PROJECT_MANAGER= "Project Manager","Project Manager"

class CustomUser(AbstractUser):
    role= models.CharField(max_length=50,choices=Role.choices, default=Role.COUSTOMER)