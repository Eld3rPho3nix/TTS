from TTS.api import TTS
from flask import Flask, request, jsonify, send_file
import tempfile

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False, gpu=False)

app = Flask(__name__)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "Missing text"}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        tts.tts_to_file(text=text, speaker_wav=None, language="it", file_path=f.name)
        return send_file(f.name, mimetype="audio/wav")

@app.route("/", methods=["GET"])
def home():
    return "XTTS TTS API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
