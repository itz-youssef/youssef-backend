import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app)

# Added a home route so you can verify the server is live in your browser
@app.route('/')
def home():
    return "Youssef's AI Backend is Online!"

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_message = user_data.get("message")

    response = client.models.generate_content(
        model="gemini-3.0-flash",
        contents=user_message,
        config={
            "system_instruction": """
            You are Youssef Yasser's AI Assistant. 
            Background: Youssef is a CS student at Cairo University (2023-2027). 
            Expertise: AI Development, Deep Learning (Neural Networks), and Software Engineering.
            Achievements: Honorable Mention in ICPC ECPC, CU AI Nexus 2025 attendee.
            Tone: Professional and enthusiastic about AI. 
            Constraint: Only answer questions related to Youssef's career, projects, and skills.
            """
        }
    )
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)
