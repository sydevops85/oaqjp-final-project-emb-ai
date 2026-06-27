import requests


def emotion_detector(input_text: str) -> dict:
    """
    Analyze text using Watson Emotion API and return simplified emotion scores.

    Args:
        input_text (str): The text string to analyze.

    Returns:
        dict: Dictionary containing emotion scores and dominant emotion.
    """
    # API endpoint for Watson Emotion service
    api_url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Required headers including model ID
    request_headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    }

    # Payload containing the text to analyze
    request_payload = {
        "raw_document": {
            "text": input_text
        }
    }

    try:
        # Send POST request to the API
        response = requests.post(
            api_url,
            headers=request_headers,
            json=request_payload,
            timeout=10
        )
        response.raise_for_status()

        # Parse JSON response
        response_data = response.json()

        # Extract emotion scores from the first prediction
        emotion_scores = response_data["emotionPredictions"][0]["emotion"]

        # Find dominant emotion (highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return simplified dictionary
        return {
            "anger": emotion_scores.get("anger", 0.0),
            "disgust": emotion_scores.get("disgust", 0.0),
            "fear": emotion_scores.get("fear", 0.0),
            "joy": emotion_scores.get("joy", 0.0),
            "sadness": emotion_scores.get("sadness", 0.0),
            "dominant_emotion": dominant_emotion,
        }

    except requests.exceptions.RequestException as error:
        # Return error details in case of failure
        return {"error": str(error)}