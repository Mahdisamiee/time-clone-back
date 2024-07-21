import json
from deep_translator import GoogleTranslator

# Load the JSON file
with open('en.json', 'r') as file:
    data = json.load(file)

# Create a translator object
translator = GoogleTranslator(source='auto', target='ru')

new_data = dict()


def translate_values(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                translate_values(value)
            elif isinstance(value, str):
                data[key] = translator.translate(value, lang_tgt='ru')
    elif isinstance(data, str):
        data = translator.translate(data, lang_tgt='ru')

translate_values(data)

# Save the translated data back to the JSON file
with open('ru.json', 'w') as file:
    json.dump(data, file, indent=2)

print("Translation complete. Saved to ru.json")