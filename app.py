from flask import Flask, request, render_template
from PIL import Image
import pytesseract

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    extracted_text = ""

    if request.method == "POST":
        file = request.files.get("image")

        if file:
            img = Image.open(file.stream)   # <-- in memory
            extracted_text = pytesseract.image_to_string(img)

    return render_template("index.html", text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True)
