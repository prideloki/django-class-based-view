from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GlobalPermissionManager(models.Manager):

    def get_query_set(self):
        return super(GlobalPermissionManager, self).\
            get_query_set().filter(content_type__name='global_permission')


class GlobalPermission(Permission):

    """A global permission, not attached to a model"""

    objects = GlobalPermissionManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        ct, created = ContentType.objects.get_or_create(app_label='global')
        self.content_type = ct
        super(GlobalPermission, self).save(*args, **kwargs)
