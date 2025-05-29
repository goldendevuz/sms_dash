import json
from django.shortcuts import render, redirect
from django.contrib import messages
from icecream import ic
import requests

from .forms import SendMessageForm

from .models import *

def index(request):
  context = {
    'segment': 'dashboard'
  }
  return render(request, "pages/index.html", context)

# Components
def color(request):
  context = {
    'segment': 'color'
  }
  return render(request, "pages/color.html", context)

def typography(request):
  context = {
    'segment': 'typography'
  }
  return render(request, "pages/typography.html", context)

def icon_feather(request):
  context = {
    'segment': 'feather_icon'
  }
  return render(request, "pages/icon-feather.html", context)

def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

def send_sms_message(api_token, html_message, phone):
    url = "https://piglet-factual-mentally.ngrok-free.app/api/sms/"

    payload = json.dumps({
    "number": phone.replace("+998", ""),
    "text": f"""{html_message}""",
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}',
    }
    ic(payload)
    ic(headers)

    response = requests.request("POST", url, headers=headers, data=payload)
    ic(response)
    ic(response.json())
    return response.json()

def send_message_view(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            api_token = form.cleaned_data['api_token']
            phone_number = form.cleaned_data['phone_number']
            message_text = form.cleaned_data['message']

            response = send_sms_message(api_token, message_text, phone_number)

            # Simulate sending a message (or integrate your API here)
            print(f"Sending message to {phone_number} using token {api_token}")
            print(f"Message: {message_text}")
            print(f"Response: {response}")

            messages.success(request, "Message sent successfully!")
            return redirect('send_message')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SendMessageForm()

    return render(request, 'pages/sample-page.html', {'form': form})
