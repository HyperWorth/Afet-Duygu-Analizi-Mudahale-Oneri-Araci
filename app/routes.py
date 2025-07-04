from flask import Blueprint, render_template, request
from .gemini_api import analyze_emotion
import re


def extract_score(text):
    try:
        match = re.search(r"Skor[:：]?\s*(\d+)", text)
        if match:
            return int(match.group(1))
    except:
        pass
    return 0

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    results = []
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            lines = [line.strip() for line in user_input.split('\n') if line.strip()]
            for line in lines:
                ai_output = analyze_emotion(line)
                score = extract_score(ai_output)

                # Sınıf belirle
                if score >= 80:
                    card_class = "high-risk"
                elif score >= 60:
                    card_class = "mid-risk"
                else:
                    card_class = "low-risk"

                results.append({
                    "input": line,
                    "output": ai_output,
                    "score": score,
                    "card_class": card_class
                })             

    return render_template("index.html", results=results, user_input=user_input)
