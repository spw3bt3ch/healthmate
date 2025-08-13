
from dataclasses import dataclass

@dataclass
class Result:
    value: str
    category: str
    message: str

def bmi(weight_kg: float, height_m: float) -> Result:
    bmi_val = weight_kg / (height_m ** 2)
    if bmi_val < 18.5:
        cat = "Underweight"
        msg = "Eat a balanced diet and consider consulting a nutritionist."
    elif 18.5 <= bmi_val <= 24.9:
        cat = "Normal weight"
        msg = "Maintain your healthy lifestyle!"
    elif 25 <= bmi_val <= 29.9:
        cat = "Overweight"
        msg = "Increase physical activity and watch your diet."
    else:
        cat = "Obese"
        msg = "Consult your doctor for a weight loss plan."
    return Result(value=f"{bmi_val:.1f}", category=cat, message=msg)

def whr(waist_cm: float, hip_cm: float, gender: str) -> Result:
    whr_val = waist_cm / hip_cm
    gender = (gender or '').strip().upper()
    if gender == "M":
        if whr_val < 0.90:
            cat, msg = "Low risk", "Maintain healthy habits."
        elif 0.90 <= whr_val <= 0.99:
            cat, msg = "Moderate risk", "Consider lifestyle adjustments."
        else:
            cat, msg = "High risk", "Consult a doctor for assessment."
    else:  # default to F thresholds if not M
        if whr_val < 0.80:
            cat, msg = "Low risk", "Maintain healthy habits."
        elif 0.80 <= whr_val <= 0.89:
            cat, msg = "Moderate risk", "Consider lifestyle adjustments."
        else:
            cat, msg = "High risk", "Consult a doctor for assessment."
    return Result(value=f"{whr_val:.2f}", category=cat, message=msg)

def bmr(weight_kg: float, height_cm: float, age_years: int, gender: str) -> Result:
    gender = (gender or '').strip().upper()
    if gender == "M":
        bmr_val = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
    else:
        bmr_val = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) - 161
    return Result(value=f"{bmr_val:.0f}", category="kcal/day", message="Energy needed at rest (Mifflin-St Jeor).")

def stroke_score(age: int, high_bp: bool, smoker: bool, diabetes: bool, high_chol: bool, inactive: bool) -> Result:
    score = 0
    if age >= 55: score += 2
    if high_bp: score += 2
    if smoker: score += 2
    if diabetes: score += 2
    if high_chol: score += 1
    if inactive: score += 1

    if score <= 2:
        cat, msg = "Low risk", "Great! Keep up healthy habits."
    elif 3 <= score <= 5:
        cat, msg = "Moderate risk", "Consider lifestyle changes and routine checkups."
    else:
        cat, msg = "High risk", "Please consult your doctor for evaluation."
    return Result(value=f"{score}", category=cat, message=msg)

def arthritis_score(joint_pain: bool, morning_stiffness: bool, swelling: bool, family_history: bool, difficulty_moving: bool) -> Result:
    score = 0
    if joint_pain: score += 2
    if morning_stiffness: score += 2
    if swelling: score += 1
    if family_history: score += 1
    if difficulty_moving: score += 2

    if score <= 2:
        cat, msg = "Low likelihood", "Monitor your health and stay active."
    elif 3 <= score <= 5:
        cat, msg = "Possible arthritis", "Monitor symptoms and consider a checkup."
    else:
        cat, msg = "Likely arthritis", "See a doctor soon."
    return Result(value=f"{score}", category=cat, message=msg)
