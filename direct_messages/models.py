from django.db import models
from common.models import TimeStampedModel as CommonModel


class ChatRoom(CommonModel):

    """Room Model Definition"""

    participants = models.ManyToManyField(
        "users.User",
        related_name="chatroom_direct_messages",
    )

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
        related_name="user_direct_messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE,
        related_name="direct_messages",
    )

    def __str__(self):
        return f"{self.user} says: {self.text}"
