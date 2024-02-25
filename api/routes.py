from api import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    return "Predict"

@app.route('/parameters', methods=['GET'])
def parameters():
    return "Parameters"

          