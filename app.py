from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_COEFFICIENTS = {
    "intercept": 50000,
    "area_coef": 3000, 
    "rooms_coef": 20000
}

@app.route('/')
def home():
    return "Welcome to the Flask Prediction API! Use the /predict endpoint to get predictions."


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  
        area = data.get('area', 0)
        rooms = data.get('rooms', 0)
        
        price = (
            MODEL_COEFFICIENTS["intercept"] +
            MODEL_COEFFICIENTS["area_coef"] * area +
            MODEL_COEFFICIENTS["rooms_coef"] * rooms
        )
        
        return jsonify({"predicted_price": price}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  

