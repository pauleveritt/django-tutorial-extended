from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from polls.models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    votes = serializers.BooleanField(required=False)

    class Meta:
        model = Choice
        fields = ("id", "choice_text", "votes")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date", "choices")

    def create(self, validated_data):
        choices = validated_data.pop("choices")
        instance = super(QuestionSerializer, self).create(validated_data)
        instance.save()
        choice_obj = [
            Choice(choice_text=item["choice_text"], question=instance)
            for item in choices
        ]
        Choice.objects.bulk_create(choice_obj)
        return instance


class VoteSerializer(serializers.Serializer):
    question_id = serializers.IntegerField(required=True)
    choice_id = serializers.IntegerField(required=True)
    vote = serializers.BooleanField(required=True)

    def validate(self, attrs):
        question_id = attrs["question_id"]
        choice_id = attrs["choice_id"]
        vote = attrs["vote"]

        if Question.objects.filter(id=question_id).exists() is False:
            raise ValidationError("This question ID does not exist !")

        if (
            Choice.objects.filter(id=choice_id, question_id=question_id).exists()
            is False
        ):
            raise ValidationError("This choice ID does not exist !")
        return attrs
