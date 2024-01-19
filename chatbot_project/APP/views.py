from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from nltk.chat.util import Chat, reflections
from django.shortcuts import render

pairs = [
    ["hey|hi|hello", ["Hello!", "Hey there!", "Hi!"]],
    ["how's it going", ["It's going well, thank you!", "Everything's good. How about you?"]],
    ["tell me a joke", ["Why did the chicken cross the road? To get to the other side!"]],
    ["what do you do", ["I'm here to chat and assist you.", "I'm a virtual assistant ready to help."]],
    ["good morning", ["Good morning!"]],
    ["how's the weather", ["I'm not sure about the current weather. You may want to check a weather app."]],
    ["what is the meaning of life", ["The meaning of life is a complex philosophical question. What do you think?"]],
    ["see you later|goodbye", ["See you later!", "Goodbye for now."]],
    ["favorite color", ["I don't have a favorite color. What's yours?"]],
    ["where are you from", ["I exist in the realm of code, so I don't have a specific location."]],

]

chatbot = Chat(pairs, reflections)

def index(request):
    return render(request,"index.htm")

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = request.POST.get('message', '')
        response = chatbot.respond(data)
        return JsonResponse({'message': response})

    return JsonResponse({'error': 'Invalid request method'})
