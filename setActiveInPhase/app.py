from flask import Flask, send_from_directory, request, jsonify, render_template
from setActiveInPhase import setActiveInPhase

app = Flask(__name__)

@app.route('/')
def index():
    # Read and return the content of the HTML file
    with open('templates/index.html', 'r') as file:
        return file.read()

@app.route('/style.css')
def styles():
    return send_from_directory('.', 'style.css')

@app.route('/submit', methods=['POST'])
def submit():
    analysis = request.form.get("analysis", "")
    shape = request.form.get("shape", "")
    shape_sets = request.form.get("shape_sets", "").split(',')  # Split input by comma
    stages = request.form.get("stages", "").split(',')  # Split input by comma
    boolean = request.form.get("boolean", "")

    results = []
    for shape_set in shape_sets:
        for stage in stages:
            result = setActiveInPhase(analysis, shape, [shape_set.strip()], [stage.strip()], boolean)
            results.extend(result)
    
        # Join the results with newline characters before passing them to the template
    result_string = '\n'.join(results)
    
    return render_template("index.html", result=result_string)



if __name__ == "__main__":
    app.run(debug=True)