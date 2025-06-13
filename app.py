import flask


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    slider100 = data.get('slider100')
    slider15 = data.get('slider15')
    print(f"Received values -> Slider 100: {slider100}, Slider 15: {slider15}")
    return jsonify({"message": "Values received!", "slider100": slider100, "slider15": slider15})

if __name__ == '__main__':
    app.run(host='', port=5000, debug=True)  # port forwarding enabled
