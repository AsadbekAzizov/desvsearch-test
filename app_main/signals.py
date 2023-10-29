from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from . import models


@receiver(signal=post_save, sender=User)
def profile_creation(sender, instance, created, **kwargs):
    if created:
        profile = models.Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
        )
        profile.save()


@receiver(signal=post_save, sender=models.Profile)
def profile_update(sender, instance, created, **kwargs):
    if not created:
        profile = instance
        user = profile.user

        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.save()


@receiver(signal=post_delete, sender=models.Profile)
def user_delete_on_profile_delete(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

# instance -> the object itself that was updated or created

# To create a profile for the user every time the user is registered
# Write a signal that listens for the user object
# Register a signals
# Look how it works












