import os
import random
import json
from django.conf import settings
from django.shortcuts import render

def index(request):
    # Define the path to the JSON file (within the static directory)
    json_path = os.path.join(settings.BASE_DIR, 'testapp/static/myapp/data/words.json')

    # Load the words from the JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Fetch the list of words
    simple_words_list = data.get('simple_words_list', [])

    # Select 10 random words from the list
    random_words = ' '.join(random.sample(simple_words_list, 10))

    return render(request, 'testapp/index.html', {'typing_text': random_words})
