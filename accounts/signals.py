from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from .models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
	 userprofile = UserProfile.objects.create(user=instance)
		