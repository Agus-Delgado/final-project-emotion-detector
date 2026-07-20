from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page with the emotion analysis form."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    text_to_analyse = request.form.get('text_to_analyse')

    if not text_to_analyse or not text_to_analyse.strip():
        return render_template('index.html', error="Please enter some text to analyze."), 400

    try:
        response = emotion_detector(text_to_analyse)

        if isinstance(response, dict) and 'status_code' in response:
            return render_template('index.html', error="Error processing the request from Watson."), 400

        return render_template('index.html',
                               anger=response.get('anger', 0),
                               disgust=response.get('disgust', 0),
                               fear=response.get('fear', 0),
                               joy=response.get('joy', 0),
                               sadness=response.get('sadness', 0),
                               dominant_emotion=response.get('dominant_emotion', 'neutral'))
    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template('index.html', error="An internal error occurred."), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
