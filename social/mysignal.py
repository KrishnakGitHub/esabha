from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from social.models import MyProfile, JobPost

import random
import string
from django.utils.text import slugify

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwarg):
    if created:
        MyProfile.objects.create(user = instance, name=instance.username)

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.company_name)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=JobPost, dispatch_uid='slug_creator')
def slug_creator(sender, instance, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)