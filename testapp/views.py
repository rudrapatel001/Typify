import requests
from django.shortcuts import render

def index(request):
    # Fetch random words from the API
    response = requests.get('https://random-word-api.herokuapp.com/word?number=10')
    if response.status_code == 200:
        random_words = ' '.join(response.json())  # Join the list of random words
    else:
        random_words = "The quick brown fox jumps over the lazy dog."  # Fallback text

    return render(request, 'testapp/index.html', {'typing_text': random_words})
