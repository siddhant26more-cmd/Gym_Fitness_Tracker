import json
import os

print("=" * 45)
print("        GYM & FITNESS TRACKER")
print("=" * 45)

print("\n1. Create Profile")
print("2. BMI Calculator")
print("3. Calorie Calculator")
print("4. Add Workout")
print("5. Add Meal")
print("6. View Summary")
print("7. Exit")

choice = input("\nEnter your choice: ")

# ---------------- CREATE PROFILE ----------------

if choice == "1":

    print("\n--- CREATE PROFILE ---")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (cm): "))
    weight = float(input("Enter your weight (kg): "))
    goal = input("Enter your fitness goal: ")

    profile = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "goal": goal
    }

    with open("profile.json", "w") as file:
        json.dump(profile, file, indent=4)

    print("\nProfile created successfully!")
    print("Name:", name)
    print("Age:", age)
    print("Height:", height, "cm")
    print("Weight:", weight, "kg")
    print("Goal:", goal)


# ---------------- BMI CALCULATOR ----------------

elif choice == "2":

    print("\n--- BMI CALCULATOR ---")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    print("\nYour BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")


# ---------------- CALORIE CALCULATOR ----------------

elif choice == "3":

    print("\n--- CALORIE CALCULATOR ---")

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))

    gender = input("Enter gender (M/F): ")

    if gender.upper() == "M":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    calories = bmr * 1.55

    print("\nEstimated daily calories:", round(calories), "kcal")


# ---------------- ADD WORKOUT ----------------

elif choice == "4":

    print("\n--- ADD WORKOUT ---")

    workout = input("Enter workout/exercise: ")
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter repetitions: "))

    workout_data = {
        "exercise": workout,
        "sets": sets,
        "reps": reps
    }

    with open("workout.json", "w") as file:
        json.dump(workout_data, file, indent=4)

    print("\nWorkout saved successfully!")


# ---------------- ADD MEAL ----------------

elif choice == "5":

    print("\n--- ADD MEAL ---")

    food = input("Enter food name: ")
    calories = float(input("Enter calories: "))
    protein = float(input("Enter protein (g): "))

    meal_data = {
        "food": food,
        "calories": calories,
        "protein": protein
    }

    with open("meal.json", "w") as file:
        json.dump(meal_data, file, indent=4)

    print("\nMeal saved successfully!")


# ---------------- VIEW SUMMARY ----------------

elif choice == "6":

    print("\n--- FITNESS SUMMARY ---")

    if os.path.exists("profile.json"):

        with open("profile.json", "r") as file:
            profile = json.load(file)

        print("\nName:", profile["name"])
        print("Age:", profile["age"])
        print("Height:", profile["height"], "cm")
        print("Weight:", profile["weight"], "kg")
        print("Goal:", profile["goal"])

    else:
        print("\nNo profile found.")
        print("Please create a profile first.")


# ---------------- EXIT ----------------

elif choice == "7":

    print("\nThank you for using Gym & Fitness Tracker!")

else:

    print("\nInvalid choice!")