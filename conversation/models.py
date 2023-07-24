from django.contrib.auth.models import User
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

class ConversationsMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name= 'messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name= 'created_messages', on_delete=models.CASCADE)

