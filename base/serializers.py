from rest_framework import serializers
from .models import Policy, Comment


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

    def validate(self, attrs):
        """
        This method checks the assigned fields required for each policy provider conditionally
        :param attrs:
        :return: attributes
        """
        field_rules = attrs["policy_provider"].fieldrule_set.all()
        for field_rule in field_rules:
            if field_rule.is_required and not attrs[field_rule.field_name]:
                raise serializers.ValidationError(
                    {field_rule.field_name: f"{field_rule.field_name} is required for {attrs['policy_provider'].name}"})
            elif not field_rule.is_required:
                attrs[field_rule.field_name] = None
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

