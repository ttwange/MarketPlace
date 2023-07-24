from django.db import models
from item.models import Items
# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Items, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-modified_At',)

