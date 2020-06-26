from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from social.models import MyProfile

import random
import string
from django.utils.text import slugify

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg):
    if created:
        MyProfile.objects.create(user = instance, name=instance.username)

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
