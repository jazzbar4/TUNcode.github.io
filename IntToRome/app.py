from flask import Flask, render_template, request, send_from_directory
from ArabToRoman import IntToRome

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route("/", methods=["POST"])
def getvalue():
    numeral = request.form["numeral"]
    numeral_int = int(numeral)
    roman_numeral = IntToRome(numeral_int)
    return render_template("index.html", n=numeral, roman=roman_numeral)

if __name__ == "__main__":
    app.run(debug=True)