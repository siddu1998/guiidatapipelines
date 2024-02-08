from django.http import JsonResponse, HttpResponseBadRequest,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from .models import *  # Ensure this is your custom User model
import json
import os
from collections import defaultdict

@csrf_exempt
def getOAI(request):
    return JsonResponse({'key':os.environ.get('oaiKey')}, safe=False, status=201)
    

@csrf_exempt
def message_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
            student_id = data.get('student_id')
            sent_by = data.get('sent_by')
            content = data.get('content')
            gpt_used = data.get('gpt_used')

            message = Message(
                session_id=session_id,
                student_id=student_id,
                sent_by=sent_by,
                content=content,
                gpt_used=gpt_used,
            )
            message.save()

            return JsonResponse({'status': 'success', 'message': 'Feedback message saved successfully'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})





@csrf_exempt  # Bypass CSRF token for simplicity, use only for testing
def feedback_message_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get('session_id')
            student_id = data.get('student_id')
            sent_by = data.get('sent_by')
            content = data.get('content')
            gpt_used = data.get('gpt_used')

            feedback_message = FeedbackMessage(
                session_id=session_id,
                student_id=student_id,
                sent_by=sent_by,
                content=content,
                gpt_used=gpt_used,
            )
            feedback_message.save()

            return JsonResponse({'status': 'success', 'message': 'Feedback message saved successfully'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


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
def list_feedback_gpts(request):
    if request.method == 'GET':
        gpts = FeedbackGPT.objects.all().values('id', 'name', 'instructions')
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
        
@csrf_exempt
def feedbackList(request):
    messages = Message.objects.all()
    grouped_messages = defaultdict(list)

    # Group messages by session_id
    for message in messages:
        grouped_messages[message.session_id].append({
            "id": message.id,
            "session_id": message.session_id,
            "student_id": message.student_id,
            "sent_by": message.sent_by,
            "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "content": message.content,
            "gpt_used": message.gpt_used,
        })

    # Convert defaultdict to dict for JSON serialization
    grouped_messages_dict = dict(grouped_messages)

    return JsonResponse(grouped_messages_dict, safe=False)  # safe=False is needed to allow non-dict objects