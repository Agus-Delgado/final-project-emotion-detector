def emotion_detector(text_to_analyse):
    if not text_to_analyse or not text_to_analyse.strip():
        return {"status_code": 400}

    # Mock para testing local
    text = text_to_analyse.lower()
    if "happy" in text or "excited" in text:
        dominant = "joy"
    elif "sad" in text or "depressed" in text:
        dominant = "sadness"
    elif "angry" in text or "frustrated" in text:
        dominant = "anger"
    elif "disgust" in text:
        dominant = "disgust"
    else:
        dominant = "joy"

    return {
        'anger': 0.1,
        'disgust': 0.1,
        'fear': 0.1,
        'joy': 0.8 if dominant == "joy" else 0.2,
        'sadness': 0.8 if dominant == "sadness" else 0.1,
        'dominant_emotion': dominant
    }
