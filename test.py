import urllib.request
import json

key = 'AIzaSyDVLHK1ZpTdGWBbdPYf6qOAboA6H875W4E'
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}'
prompt = 'You are the Magical Mood Chef. A user feels JOYFUL and prefers Indian cuisine. Generate exactly 3 recipes as a JSON array. Each object MUST exactly match this structure: { "id": "g1", "badge": "Dinner Ritual", "tag": "MAGIC", "name": "Recipe Name", "description": "Short desc", "time": "30 mins Prep", "difficulty": "Easy", "vibe": "Happy", "diet": "Vegan", "highlight": "Fresh", "icon": "spa", "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80", "midImg": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800&q=80", "tip": "Chef tip", "ingredients": [{"item": "Carrot", "amount": "1 cup"}], "steps": [{"num": 1, "title": "Chop", "desc": "Chop it"}] }. Return ONLY a valid JSON array.'

data = json.dumps({'contents': [{'parts': [{'text': prompt}]}]}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        text = result['candidates'][0]['content']['parts'][0]['text']
        print('SUCCESS')
        print(text[:200])
except Exception as e:
    print('ERROR:', str(e))
