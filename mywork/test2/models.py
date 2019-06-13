from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpubtitle = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle