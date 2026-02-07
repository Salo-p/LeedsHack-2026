import os
import csv
from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
#import google.generativeai as genai

from PIL import Image

load_dotenv()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

os.makedirs("uploads", exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["slide"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    image = Image.open(filepath)

    prompt = """
Analyze this lecture slide.

1. Write a short, student-friendly summary
2. Generate 3 thoughtful questions a student could ask the lecturer

Respond in JSON format:
{
  "summary": "...",
  "questions": ["...", "...", "..."]
}
"""

    response = model.generate_content([prompt, image])
    result = response.text.strip()

    data = eval(result)  # simple parsing (OK for prototype)

    # Save questions to CSV
    with open("questions.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for q in data["questions"]:
            writer.writerow([q])

    os.remove(filepath)

    return render_template(
        "result.html",
        summary=data["summary"],
        questions=data["questions"]
    )

if __name__ == "__main__":
    app.run(debug=True)
