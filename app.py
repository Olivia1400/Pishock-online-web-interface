from flask import Flask, render_template, request, jsonify, flash
from interface import main

app = Flask(__name__)
app.secret_key = '12'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    intensity = int(data.get('intensity'))
    duration = int(data.get('duration'))
    flash(f"Received values -> Intensity: {intensity}, Duration: {duration}")
    return jsonify({"message": "Values received!", "intensity": intensity, "duration": duration}), main(intensity, duration)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # port forwarding enabled
