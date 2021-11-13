from django.shortcuts import render
from django.http import JsonResponse

#REST Framework librairies
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Model Import
from programs.models import Task

#Serializing data
from programs.serializers import TaskSerializer



# Create your views here.
@api_view(["GET"])
def apiOverview_view(request):
    api_urls = {
    'List' : '/task-list/',
    'Detail View' : '/task-detail/<str:pk>/',
    'Create':'/task-create/',
    'Update':'/task-update/<str:pk>/',
    'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def TaskList_view(request):
    tasks = Task.objects.all()
    serialized_task = TaskSerializer(tasks, many=True)
    return Response(serialized_task.data)

@api_view(['GET'])
def TaskDetail_view(request,pk):
    try:
        query = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        query = None
        return Response({"error": "Task was not found!"}, status=404)
    return Response(TaskSerializer(query, many=False).data)

@api_view(['POST'])
def TaskCreate_view(request):
    data = request.data
    created_serialized_task = TaskSerializer(data=data)
    if created_serialized_task.is_valid():
        created_serialized_task.save()
    return Response(created_serialized_task.data)

@api_view(['POST'])
def TaskUpdate_view(request, pk):
    try:
        task_to_update = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"errors":"Task was not found!"}, status=404)
    serialized_task = TaskSerializer(instance=task_to_update, data=request.data)
    if serialized_task.is_valid():
        serialized_task.save()
    return Response(serialized_task.data)

@api_view(['DELETE'])
def TaskDelete_view(request, pk):
    try:
        task_to_delete= Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response({"errors":"Task was not found!"}, status=404)
    task_to_delete.delete()

    return Response({"response":"Task is successfully deleted!!"})
