from rest_framework import serializers

from siaknngauth.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Account

        fields = (
            'user',
            'npm',
            'faculty_id',
        )
