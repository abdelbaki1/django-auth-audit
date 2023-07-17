from rest_framework import serializers
from .models import AuthLogEntry


class AuthLogEntrySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%d %B/%Y at %H:%M:%S")

    actor = serializers.SlugRelatedField(
        read_only=True,
        slug_field="email", default='system'
    )
    action = serializers.CharField(source='get_action_display')

    class Meta:
        model = AuthLogEntry
        fields = '__all__'
