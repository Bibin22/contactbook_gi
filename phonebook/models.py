from django.db import models
import uuid


class ContactBook(models.Model):
    contact_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_user = models.CharField(max_length=200, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_user = models.CharField(max_length=200, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone_no = models.CharField(max_length=12, null=True, blank=True, unique=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.name) + str(self.phone_no)
