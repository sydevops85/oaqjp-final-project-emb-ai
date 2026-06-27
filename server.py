"""
Flask application for emotion detection.
Serves a web interface and provides an API endpoint
to analyze text and return emotion scores.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Render the main index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_det():
    """
    Handle emotion detection requests.
    Accepts a query parameter 'textToAnalyze' and returns
    formatted emotion scores with the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Treat blank or whitespace-only input as invalid
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 200

    result = emotion_detector(text_to_analyze)

    # Handle invalid text case (dominant_emotion is None)
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 200

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
