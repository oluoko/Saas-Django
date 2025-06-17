from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("enterprise", "Enterprise perm"), # subscriptions.enterprise
            ("pro", "Pro perm"), # subscriptions.pro
            ("basic", "Basic perm"), # subscriptions.basic
            ("free", "Free perm"),  # subscriptions.free
        ]