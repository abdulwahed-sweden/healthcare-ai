from django.shortcuts import render
from django.conf import settings
from openai import OpenAI

def home(request):
    result = ""
    if request.method == "POST":
        input_text = request.POST.get("user_text", "")

        client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": input_text},
            ],
            stream=False,
            max_tokens=60  # عشان يكون الرد قصير
        )

        result = response.choices[0].message.content

    return render(request, "pages/home.html", {"result": result})



def about(request):
    context = {
        'title': 'About Us',
        'about_text': 'We provide AI-powered healthcare solutions.'
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    context = {
        'title': 'Contact Us',
        'contact_email': 'info@healthcare-ai.com'
    }
    return render(request, 'pages/contact.html', context)