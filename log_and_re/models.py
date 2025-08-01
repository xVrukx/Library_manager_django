from django.db import models
from django.contrib.auth.hashers import make_password

class register(models.Model):
    username = models.TextField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    password = models.TextField(max_length=100)
    number = models.IntegerField(blank=True, null=True)

    
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)