from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_customer = models.BooleanField(default=False)
    image=models.ImageField(upload_to="profile_imgs/",null=True)
    is_manager = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null=False)
    city=models.CharField(max_length=15, null=False)
    postalcode=models.CharField(max_length=15, null=False)
    # postalcodes=models.CharField(max_length=15, null=False)





class UserProfile(models.Model):
    auth_token = models.CharField(max_length=100 )  
    is_active = models.BooleanField(default = True)
    # is_actives = models.BooleanField(default = True)
    has_profile = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    captcha_score = models.FloatField(default = 0.0)

    def __str__(self):
        return f'{self.user}'


