from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "choice_text", "votes")


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date", "choices")


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

        if Choice.objects.filter(id=choice_id, question_id=question_id).exists() is False:
            raise ValidationError("This choice ID does not exist !")
        return attrs


