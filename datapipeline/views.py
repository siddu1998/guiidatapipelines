from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from .models import *  # Ensure this is your custom User model
import json
import os

@csrf_exempt
def getOAI(request):
    return JsonResponse({'key':os.environ.get('oaiKey')}, safe=False, status=201)
    

@csrf_exempt
def message_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            # Parsing and validating data
            session_id = data.get('session_id')
            student_id = data.get('student_id')  # Expect assigned_id instead of user_id
            content = data.get('content')

            # Ensuring all necessary data is provided
            if not all([session_id, student_id, content]):
                return HttpResponseBadRequest("Missing required fields")

            # Creating the message
            message = Message(
                session_id=session_id,
                student_id=student_id,
                content=content,
            )
            message.save()

            # Returning the created message data
            return JsonResponse({
                "id": message.id,
                "session_id": message.session_id,
                "student_id": message.student_id,
                "content": message.content,
            })

        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")

    return HttpResponseBadRequest("Invalid request method")


@csrf_exempt  # For simplicity, but handle CSRF properly in production
def create_new_gpt(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_gpt = CustomGPT(
                name=data['name'],
                created_by=data['created_by'],
                university=data['university'],
                gpt_type=data['gpt_type'],
                instructions=data['instructions']
            )
            new_gpt.save()
            return JsonResponse({"message": "Custom GPT created successfully", "id": new_gpt.id})
        except Exception as e:
            return HttpResponse(status=400, content="Error in creating Custom GPT: " + str(e))
    else:
        return HttpResponse(status=405, content="Method not allowed")


@csrf_exempt
def list_custom_gpts(request):
    if request.method == 'GET':
        gpts = CustomGPT.objects.all().values('id', 'name', 'instructions')
        return JsonResponse(list(gpts), safe=False)
    else:
        return HttpResponse(status=405, content="Method not allowed")
    

@csrf_exempt
def sendFireData(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            fireDataInstance = FireData.objects.create(data=data)
            return JsonResponse(fireDataInstance.data, safe=False, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
