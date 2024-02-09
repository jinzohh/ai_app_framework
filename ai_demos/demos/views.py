from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils import timezone
from django.db.models import Q
from django.conf import settings
from .models import Chatbot, Inputoutput
from .forms import ChatbotForm, InputOutputForm
from openai import OpenAI
import openai

def index(request):
    
    context = {
        # some variable to be referenced from html page
    }

    return render(request, 'demos/index.html', context)

def ChatBot(request):
    
    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )

    if request.method == 'POST':
        form = ChatbotForm(request.POST)

        if form.is_valid():
            # Pulling the input message entered by user
            user_msg = form.cleaned_data['msg']

            messages = [
                {
                    'role': 'system',
                    'content': 'You are an intelligent assistant',
                },
                {
                    'role': 'user',
                    'content': user_msg,
                }
            ]

            try:
                res = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=2048,    # Higher the number, more complex the response
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                chat_output = res.choices[0].message.content

                # Save conversation to backend database
                Chatbot.objects.create(
                    inputMsg=user_msg,
                    outputMsg=chat_output,
                )

                data = {
                    'output': chat_output,
                }

                return JsonResponse(data)
            
            except openai.APIError as e:
                error_msg = str(e)

                data = {
                    'error_msg': error_msg,
                }

                return JsonResponse(data)

        else:
            print("Form invalid.")
    
    else:
        form = ChatbotForm()

    chat_records = Chatbot.objects.all().order_by('timestamp')
    
    context = {
        'form': form,
        'records': chat_records,
    }

    return render(request, 'demos/chatBot.html', context)

def InputOutput(request):
    time_stamp = timezone.now()

    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )

    if request.method == 'POST':
        form = InputOutputForm(request.POST)

        if form.is_valid():
            # Pulling the input message entered by user
            user_msg1 = form.cleaned_data['msg1']
            user_msg2 = form.cleaned_data['msg2']
            user_msg3 = form.cleaned_data['msg3']
            user_msg4 = form.cleaned_data['msg4']

            messages = [
                {
                    'role': 'system',
                    'content': 'You are an intelligent assistant',  # Change this to fit need
                },
                {
                    'role': 'user',
                    'content': user_msg1,
                },
                {
                    'role': 'user',
                    'content': user_msg2,
                },
                {
                    'role': 'user',
                    'content': user_msg3,
                },
                {
                    'role': 'user',
                    'content': user_msg4,
                }
            ]

            try:
                res = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    max_tokens=2048,    # Higher the number, more complex the response
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                output_msg = res.choices[0].message.content

                # Save conversation to backend database
                Inputoutput.objects.create(
                    inputMsg1=user_msg1,
                    inputMsg2=user_msg2,
                    inputMsg3=user_msg3,
                    inputMsg4=user_msg4,
                    outputMsg1=output_msg,
                    timestamp=time_stamp,
                )

                data = {
                    'output': output_msg,
                }

                return JsonResponse(data)
            
            except openai.APIError as e:
                error_msg = str(e)

                data = {
                    'error_msg': error_msg,
                }

                return JsonResponse(data)

        else:
            print("Form invalid.")
    
    else:
        form = InputOutputForm()

    try:
        last_response = Inputoutput.objects.all().order_by('timestamp')[0]
    except IndexError as e:
        last_response = None
        pass
    
    context = {
        'form': form,
        'record': last_response,
    }

    return render(request, 'demos/inputOutput.html', context)



