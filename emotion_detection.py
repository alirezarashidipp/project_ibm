import requests

def emotion_detector(text_to_analyze):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_ID/v1/analyze"
    
    params = {
        "version": "2021-08-01"
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(url, json=data, params=params, headers=headers, auth=("apikey", "YOUR_API_KEY"))

    if response.status_code == 200:
        emotions = response.json()["emotion"]["document"]["emotion"]
        return emotions
    else:
        return None
