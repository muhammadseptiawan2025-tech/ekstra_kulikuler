import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class pengguna(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'administrator'),
        ('pembina', 'calon pembina'),
    )

    # menggunakan UUID untuk keamanan data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='PEMBINA')  

    # kolom email dibuat unique untuk persiapan login yang bisa memakai username ATAU email
    email = models.EmailField(unique=True)


def __str__(self):
    return f"{self.username} - {self.get_role_display()}"
    


