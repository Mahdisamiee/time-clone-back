def convert_cyrillic_to_latin(text):
    cyrillic_to_latin = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    
    result = ''
    for char in text:
        if char.lower() in cyrillic_to_latin:
            result += cyrillic_to_latin[char.lower()]
        else:
            result += char
    print(result.encode('latin-1').decode('unicode-escape'))
    
    return result.encode('latin-1').decode('unicode-escape')

# Open the input file
with open('ru-tmp.json', 'r') as file:
    content = file.read()

# Convert Cyrillic characters to Latin
converted_content = convert_cyrillic_to_latin(content)

# Write the converted content to the output file
with open('ru.json', 'w', encoding="utf-8") as file:
    file.write(converted_content)

print("Conversion complete. Output saved to 'ru.json'.")