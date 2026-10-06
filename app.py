from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -----------------------------
# FITNESS DATA
# -----------------------------

profile = {
    "name": "Siddhant",
    "age": 21,
    "height": 178,
    "weight": 68,
    "goal": "Muscle Gain"
}

workouts = []
meals = []


# -----------------------------
# DASHBOARD
# -----------------------------

@app.route("/")
def home():

    height_m = profile["height"] / 100
    bmi = profile["weight"] / (height_m * height_m)

    if bmi < 18.5:
        bmi_status = "Underweight"
    elif bmi < 25:
        bmi_status = "Normal"
    elif bmi < 30:
        bmi_status = "Overweight"
    else:
        bmi_status = "Obese"

    total_calories = 0
    total_protein = 0

    for meal in meals:
        total_calories += meal["calories"]
        total_protein += meal["protein"]

    return render_template(
        "index.html",
        profile=profile,
        bmi=round(bmi, 1),
        bmi_status=bmi_status,
        total_calories=total_calories,
        total_protein=total_protein,
        workouts=workouts,
        meals=meals
    )


# -----------------------------
# UPDATE PROFILE
# -----------------------------

@app.route("/profile", methods=["POST"])
def update_profile():

    profile["name"] = request.form["name"]
    profile["age"] = int(request.form["age"])
    profile["height"] = float(request.form["height"])
    profile["weight"] = float(request.form["weight"])
    profile["goal"] = request.form["goal"]

    return redirect(url_for("home"))


# -----------------------------
# ADD WORKOUT
# -----------------------------

@app.route("/workout", methods=["POST"])
def add_workout():

    workout = {
        "exercise": request.form["exercise"],
        "sets": request.form["sets"],
        "reps": request.form["reps"]
    }

    workouts.append(workout)

    return redirect(url_for("home"))


# -----------------------------
# ADD MEAL
# -----------------------------

@app.route("/meal", methods=["POST"])
def add_meal():

    meal = {
        "food": request.form["food"],
        "calories": float(request.form["calories"]),
        "protein": float(request.form["protein"])
    }

    meals.append(meal)

    return redirect(url_for("home"))


# -----------------------------
# RUN APPLICATION
# -----------------------------

# ----------------------------
# PROGRESS PAGE
# ----------------------------

@app.route("/progress")
def progress():
    # Calculate BMI
    height_m = profile["height"] / 100
    bmi = round(profile["weight"] / (height_m * height_m), 1)

    total_workouts = len(workouts)
    total_meals = len(meals)

    total_calories = sum(meal["calories"] for meal in meals)
    total_protein = sum(meal["protein"] for meal in meals)

    return render_template(
        "index.html",
        profile=profile,
        bmi=bmi,
        workouts=workouts,
        meals=meals,
        total_calories=total_calories,
        total_protein=total_protein
    )
    total_workouts = len(workouts)
    total_meals = len(meals)

    total_calories = sum(meal["calories"] for meal in meals)
    total_protein = sum(meal["protein"] for meal in meals)

    return render_template(
        "index.html",
        profile=profile,
        bmi=bmi,
        workouts=workouts,
        meals=meals,
        total_calories=total_calories,
        total_protein=total_protein
    )


# ----------------------------
# RUN APPLICATION
# ----------------------------

if __name__ == "__main__":
    app.run(debug=True)