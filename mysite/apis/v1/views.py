from django.db.models import Max
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Choice, Question

from . import serializers


class QuestionAPI(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class QuestionRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(id=self.kwargs.get("pk", None))

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(
            {"status": True, "message": "Question Updated !", "data": serializer.data}
        )


class ChoiceVoteAPI(APIView):
    def post(self, request):
        post_data = request.data
        serializer = serializers.VoteSerializer(data=post_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.validated_data
            print(valid_data["question_id"])
            choice_obj = Choice.objects.filter(
                question_id=valid_data["question_id"], id=valid_data["choice_id"]
            )
            max_votes = choice_obj.aggregate(Max("votes"))["votes__max"]
            if valid_data["vote"]:
                vote_count = max_votes + 1
            else:
                if max_votes <= 0:
                    vote_count = 0
                else:
                    vote_count = max_votes - 1
            choice_obj.update(votes=vote_count)
        return Response(
            {"status": True, "message": "Voted Successfully !", "data": None},
            status=status.HTTP_201_CREATED,
        )
