from django.db.models import Max
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Question, Choice
from . import serializers


@api_view(['GET'])
def question_list(request):
    if request.method == 'GET':
        queryset = Question.objects.all()
        serializer = serializers.QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def question_post(request):
    if request.method == 'POST':
        serializer = serializers.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def question_retrieve(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({"status": False, "message": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.QuestionSerializer(question)
        return Response({"status": True, "data": serializer.data})


@api_view(["PUT"])
def question_update(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({"status": False, "message": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method in ('PUT', 'PATCH'):
        partial = request.method == 'PATCH'
        serializer = serializers.QuestionSerializer(question, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": True, "message": "Question Updated!", "data": serializer.data})


@api_view(["DELETE"])
def question_delete(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({"status": False, "message": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        question.delete()
        return Response({"status": True, "message": "Question Deleted!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def choice_vote(request):
    post_data = request.data
    serializer = serializers.VoteSerializer(data=post_data)
    if serializer.is_valid(raise_exception=True):
        valid_data = serializer.validated_data
        choice_obj = Choice.objects.filter(question_id=valid_data["question_id"], id=valid_data["choice_id"])
        max_votes = choice_obj.aggregate(Max('votes'))['votes__max']
        if valid_data["vote"]:
            vote_count = max_votes + 1
        else:
            if max_votes <= 0:
                vote_count = 0
            else:
                vote_count = max_votes - 1
        choice_obj.update(votes=vote_count)
    return Response({"status": True, "message": "Voted Successfully !", "data": None}, status=status.HTTP_201_CREATED)
