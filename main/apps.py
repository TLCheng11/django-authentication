import imp
from unicodedata import name
from django.apps import AppConfig
from django.conf import settings

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # new function to add user to default grp when created
    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender, **kwargs):
            # get the newly created user instance
            user = kwargs["instance"]

            if kwargs["created"]:
                # check if the default exist
                group, ok = Group.objects.get_or_create(name="default")
                # add user to group
                group.user_set.add(user)

        # when the post or save is called, call the add_to_default_group function
        post_save.connect(add_to_default_group, sender=settings.AUTH_USER_MODEL)