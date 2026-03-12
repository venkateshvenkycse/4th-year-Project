from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load disease dataset
with open("diseases.json") as f:
    diseases = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    response = {
        "description": "Disease not found.",
        "precautions": "Please consult a doctor.",
        "diet": "Maintain a balanced diet."
    }

    for disease in diseases:
        if disease in user_message:
            response = diseases[disease]
            break

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)