from django.db import models

from app_main.models import Profile


class Message(models.Model):
    sender = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_messages')
    receiver = models.ForeignKey(to=Profile, on_delete=models.PROTECT, related_name='received_messages')
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject[0:10]} ... - {self.body[0:20]} ...'

    # profile.sent_messages.all()
    # profile.received_messages.all()
