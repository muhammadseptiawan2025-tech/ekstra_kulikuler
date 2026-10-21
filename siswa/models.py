from django.db import models

# Create your models here.
import uuid
from django.db import models

class siswa(models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=100)
    kelas = models.IntegerField(default=0)

    class meta:
        verbose_name_plural = "siswa"

    def __str__(self):
        return f"{self.nama} - {self.kelas}"