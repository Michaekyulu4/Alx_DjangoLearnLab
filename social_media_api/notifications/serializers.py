# notifications/serializers.py
from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target_repr', 'unread', 'timestamp']
        read_only_fields = ['id', 'actor_username', 'timestamp']

    def get_target_repr(self, obj):
        if obj.target is None:
            return None
        # Basic representation; customize as needed
        return str(obj.target)
