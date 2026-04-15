from flask import Flask, render_template, request
from model import analyze_sentiment
from database import save_review, get_all_reviews

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)

        save_review({
            "text": text,
            "sentiment": result["label"],
            "score": result["score"]
        })

    reviews = get_all_reviews()
    return render_template("index.html", result=result, reviews=reviews)

if __name__ == "__main__":
    app.run(debug=True)