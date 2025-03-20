from flask import Flask, render_template, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.json
    height = float(data.get('height', 0))  # height in meters
    weight = float(data.get('weight', 0))  # weight in kg
    
    bmi_result = calculate_bmi(height, weight)
    
    # Déterminer la catégorie de BMI
    category = ""
    if bmi_result < 18.5:
        category = "Insuffisance pondérale"
    elif 18.5 <= bmi_result < 25:
        category = "Poids normal"
    elif 25 <= bmi_result < 30:
        category = "Surpoids"
    else:
        category = "Obésité"
    
    return jsonify({
        'bmi': bmi_result,
        'category': category
    })

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.json
    height = float(data.get('height', 0))  # height in cm
    weight = float(data.get('weight', 0))  # weight in kg
    age = int(data.get('age', 0))          # age in years
    gender = data.get('gender', '').lower() # 'male' or 'female'
    
    bmr_result = calculate_bmr(height, weight, age, gender)
    
    return jsonify({
        'bmr': bmr_result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)