from rest_framework import serializers
from .models import User, Conversation, Message

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'firstname', 'lastname', 'email',
            'phone_number', 'role', 'created_at'
        ]

#Message serializer
class MessageSerializer(serializers.ModelSerializer):
    sender =UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']
    
    # Conversation  serializer
    class ConversationSerialize(serializers.ModelSerialiser):
        paticipants = UserSerializer(many=True, read_only=True)
        Messages = MessageSerializer(mny=True, read_only=True)

        class Meta:
            model = Coversation
            fields = ['conversation_id', 'participants', 'messages', 'created_at']