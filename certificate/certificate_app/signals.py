from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import Registration
from django.conf import settings


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_registration(sender,instance,created,**kwargs):
    if created:
        Registration.objects.create(user=instance)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def save_registration(sender,instance,**kwargs):
    instance.registration.save()