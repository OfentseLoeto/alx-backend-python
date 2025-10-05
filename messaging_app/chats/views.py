from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer


# Conversation ViewSet
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation and add participants.
        Expected JSON:
        {
            "participants": [1, 2, 3]
        }
        """
        participants_ids = request.data.get("participants", [])
        if not participants_ids:
            return Response(
                {"error": "Participants are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        conversation = Conversation.objects.create()
        conversation.participants.set(User.objects.filter(id__in=participants_ids))
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"])
    def send_message(self, request, pk=None):
        """
        Send a message in an existing conversation.
        Example JSON:
        {
            "sender": 1,
            "message_body": "Hello!"
        }
        """
        conversation = self.get_object()
        sender_id = request.data.get("sender")
        message_body = request.data.get("message_body")

        if not sender_id or not message_body:
            return Response(
                {"error": "Sender and message_body are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        sender = get_object_or_404(User, id=sender_id)
        message = Message.objects.create(
            sender=sender,
            conversation=conversation,
            message_body=message_body
        )

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Message ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

