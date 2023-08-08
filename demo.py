import json
xy = []
with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)
    xy.append(intents)


print(xy)
