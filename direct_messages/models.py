from django.db import models
from common.models import TimeStampedModel as CommonModel


class ChatRoom(CommonModel):

    """Room Model Definition"""

    participants = models.ManyToManyField("users.User")

    def __str__(self):
        return "Chat Room:"

class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"