from django.db import models
from django.utils import timezone

from plusoneauthentication.models import PlusOneUser


class AppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    deleted = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.modified = timezone.now()
        super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        # self.deleted = True
        # self.save()
        self.force_delete()

    def force_delete(self, using=None, keep_parents=False):
        super().delete(using, keep_parents)


class UserAppBaseModel(AppBaseModel):
    user = models.ForeignKey(PlusOneUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UniqueUserAppBaseModel(AppBaseModel):
    user = models.OneToOneField(PlusOneUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True
