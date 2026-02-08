import os
import csv
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

# setup key, do not push to git (pls)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

os.makedirs("uploads", exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    # save file
    file = request.files["slide"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:
        image = Image.open(filepath)

        prompt = """
        Analyse this lecture slide.
        1. Write a short, student-friendly summary
        2. Generate 3 thoughtful questions a student could ask the lecturer

        Respond strictly in JSON format:
        {
          "summary": "...",
          "questions": ["...", "...", "..."]
        }
        """

        # create response
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=[prompt, image]
        )

        raw_text = response.text.strip()
        clean_json = raw_text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_json)

        # save questions to CSV
        with open("questions.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for q in data["questions"]:
                writer.writerow([q])

        # result page
        return render_template(
            "result.html",
            summary=data["summary"],
            questions=data["questions"]
        )

    except Exception as e:
        print(f"Error: {e}")
        return f"Something went wrong: {e}", 500

    finally:
        # delete the file after processing
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == "__main__":
    app.run(debug=True)

'''

python -m pip install -U google-genai



'''