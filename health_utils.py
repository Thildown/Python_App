def calculate_bmi(height, weight):
    """
    Calculate Body Mass Index (BMI) given height in meters and weight in kilograms.
    
    BMI = weight (kg) / (height (m))^2
    
    Args:
        height (float): Height in meters
        weight (float): Weight in kilograms
    
    Returns:
        float: BMI value rounded to 2 decimal places
    """
    if height <= 0 or weight <= 0:
        raise ValueError("La taille et le poids doivent être positifs")
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    
    For males:
    BMR = 88.362 + (13.397 × weight (kg)) + (4.799 × height (cm)) - (5.677 × age (years))
    
    For females:
    BMR = 447.593 + (9.247 × weight (kg)) + (3.098 × height (cm)) - (4.330 × age (years))
    
    Args:
        height (float): Height in centimeters
        weight (float): Weight in kilograms
        age (int): Age in years
        gender (str): 'male' or 'female'
    
    Returns:
        float: BMR value rounded to 2 decimal places
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("La taille, le poids et l'âge doivent être positifs")
    
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Le genre doit être 'male' ou 'female'")
    
    return round(bmr, 2)