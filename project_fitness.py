
# Function to calculate macros based on user inputs
def calculate_macros(weight, calories, protein_ratio, carb_ratio, fat_ratio):
    # Ensure the ratios add up to 1 (100%)
    total_ratio = protein_ratio + carb_ratio + fat_ratio
    if total_ratio != 1:
        raise ValueError("The ratios must add up to 1 (100%).")

    # Calculate grams of each macro
    protein = (calories * protein_ratio) / 4  # 1g protein = 4 calories
    carbs = (calories * carb_ratio) / 4  # 1g carb = 4 calories
    fats = (calories * fat_ratio) / 9  # 1g fat = 9 calories

    return protein, carbs, fats


# Input data from user
weight = float(input("Enter your weight in pounds: "))
goal = input("Enter your fitness goal (bulking/cutting/maintenance): ").lower()
activity_level = input("Enter your activity level (low/moderate/high): ").lower()

# Calculate total calories based on activity level
if activity_level == "low":
    calories = weight * 12
elif activity_level == "moderate":
    calories = weight * 15
else:
    calories = weight * 18

# Ask if the user wants to customize their ratios
customize_ratios = input("Do you want to customize your macro ratios? (yes/no): ").lower()

if customize_ratios == "yes":
    protein_ratio = float(input("Enter your protein ratio (e.g., 0.3 for 30%): "))
    carb_ratio = float(input("Enter your carb ratio (e.g., 0.5 for 50%): "))
    fat_ratio = float(input("Enter your fat ratio (e.g., 0.2 for 20%): "))
else:
    # Default ratios based on the goal
    if goal == "bulking":
        protein_ratio = 0.25
        carb_ratio = 0.5
        fat_ratio = 0.25
    elif goal == "cutting":
        protein_ratio = 0.3
        carb_ratio = 0.4
        fat_ratio = 0.3
    else:  # maintenance
        protein_ratio = 0.25
        carb_ratio = 0.45
        fat_ratio = 0.3

# Calculate and display macros
try:
    protein, carbs, fats = calculate_macros(weight, calories, protein_ratio, carb_ratio, fat_ratio)
    print(f"Based on your goal of {goal} and activity level {activity_level}:")
    print(f"Total daily calories: {calories:.2f}")
    print(f"Protein: {protein:.2f} grams")
    print(f"Carbs: {carbs:.2f} grams")
    print(f"Fats: {fats:.2f} grams")
except ValueError as e:
    print(e)


    #needs to have an entry where you can enter your calories. 
    #it just calculated my macros based off me bulking, but the calories were too high which would've resulted in fat gain.